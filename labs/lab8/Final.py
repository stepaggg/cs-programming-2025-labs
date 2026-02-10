import json
import os
from datetime import datetime
from typing import Dict, List, Optional

# Константы
DATA_FILE = "azs_data.json"
PRICES = {
    "АИ-92": 57.50,
    "АИ-95": 58.30,
    "АИ-98": 64.20,
    "ДТ": 56.80
}

class Cistern:
    def __init__(self, fuel_type: str, max_volume: float, min_level_percent: float = 10.0):
        self.fuel_type = fuel_type
        self.max_volume = max_volume
        self.current_volume = max_volume * 0.5  # Начинаем с 50% заполнения
        self.min_level = max_volume * (min_level_percent / 100)
        self.is_enabled = True
        self.id = f"{fuel_type}_{id(self)}"[-6:]
    
    def to_dict(self):
        return {
            "fuel_type": self.fuel_type,
            "max_volume": self.max_volume,
            "current_volume": self.current_volume,
            "min_level": self.min_level,
            "is_enabled": self.is_enabled,
            "id": self.id
        }
    
    @classmethod
    def from_dict(cls, data):
        cistern = cls(data["fuel_type"], data["max_volume"])
        cistern.current_volume = data["current_volume"]
        cistern.min_level = data["min_level"]
        cistern.is_enabled = data["is_enabled"]
        cistern.id = data["id"]
        return cistern
    
    def can_dispense(self, amount: float) -> bool:
        return self.is_enabled and self.current_volume >= amount
    
    def dispense(self, amount: float) -> bool:
        if self.can_dispense(amount):
            self.current_volume -= amount
            # Автоматическое отключение при низком уровне
            if self.current_volume < self.min_level:
                self.is_enabled = False
            return True
        return False
    
    def refill(self, amount: float) -> bool:
        if self.current_volume + amount <= self.max_volume:
            self.current_volume += amount
            return True
        return False
    
    def get_status(self) -> str:
        status = "ВКЛ" if self.is_enabled else "ВЫКЛ"
        warning = ""
        if self.current_volume < self.min_level:
            warning = " (ниже порога)"
        elif not self.is_enabled:
            warning = " (отключена)"
        return f"{self.fuel_type} {self.id} | {self.current_volume:.0f} / {self.max_volume:.0f} л | {status}{warning}"

class FuelColumn:
    def __init__(self, column_id: int):
        self.column_id = column_id
        # Сопоставление типа топлива с цистерной
        self.fuel_connections = {}
    
    def connect_fuel(self, fuel_type: str, cistern: Cistern):
        self.fuel_connections[fuel_type] = cistern
    
    def get_available_fuels(self):
        available = []
        for fuel_type, cistern in self.fuel_connections.items():
            if cistern.is_enabled:
                available.append((fuel_type, cistern))
        return available
    
    def dispense_fuel(self, fuel_type: str, amount: float) -> Optional[float]:
        if fuel_type in self.fuel_connections:
            cistern = self.fuel_connections[fuel_type]
            if cistern.dispense(amount):
                return amount * PRICES.get(fuel_type, 0)
        return None

class AZSSystem:
    def __init__(self):
        self.cisterns = []
        self.columns = []
        self.transactions = []
        self.stats = {
            "total_cars": 0,
            "total_income": 0.0,
            "fuel_sold": {fuel: 0.0 for fuel in PRICES},
            "fuel_income": {fuel: 0.0 for fuel in PRICES},
            "refills": {fuel: 0.0 for fuel in PRICES},
            "emergency_mode": False,
            "emergency_start_time": None
        }
        self.initialize_system()
        self.load_data()
    
    def initialize_system(self):
        # Создаем цистерны
        cisterns_config = [
            ("АИ-95", 20000, 1),
            ("АИ-95", 20000, 2),
            ("АИ-92", 20000, 1),
            ("АИ-98", 15000, 1),
            ("ДТ", 25000, 1)
        ]
        
        for fuel_type, max_vol, num in cisterns_config:
            for _ in range(num):
                self.cisterns.append(Cistern(fuel_type, max_vol))
        
        # Создаем колонки (8 штук)
        for i in range(1, 9):
            column = FuelColumn(i)
            self.columns.append(column)
        
        # Настраиваем подключения колонок к цистернам
        self.setup_column_connections()
    
    def setup_column_connections(self):
        # Находим цистерны по типу
        ai95_cisterns = [c for c in self.cisterns if c.fuel_type == "АИ-95"]
        ai92_cistern = [c for c in self.cisterns if c.fuel_type == "АИ-92"][0]
        ai98_cistern = [c for c in self.cisterns if c.fuel_type == "АИ-98"][0]
        dt_cistern = [c for c in self.cisterns if c.fuel_type == "ДТ"][0]
        
        # Подключаем колонки согласно схеме
        for i, column in enumerate(self.columns):
            col_num = i + 1
            
            # АИ-95: колонки 1-4 к цистерне 1, 5-8 к цистерне 2
            if 1 <= col_num <= 4:
                column.connect_fuel("АИ-95", ai95_cisterns[0])
            elif 5 <= col_num <= 8:
                column.connect_fuel("АИ-95", ai95_cisterns[1] if len(ai95_cisterns) > 1 else ai95_cisterns[0])
            
            # АИ-92: колонки 1-6
            if 1 <= col_num <= 6:
                column.connect_fuel("АИ-92", ai92_cistern)
            
            # АИ-98: колонки 3-6
            if 3 <= col_num <= 6:
                column.connect_fuel("АИ-98", ai98_cistern)
            
            # ДТ: колонки 3-8
            if 3 <= col_num <= 8:
                column.connect_fuel("ДТ", dt_cistern)
    
    def save_data(self):
        data = {
            "cisterns": [c.to_dict() for c in self.cisterns],
            "stats": self.stats,
            "transactions": self.transactions[-100:],  # Сохраняем последние 100 транзакций
            "emergency_mode": self.stats["emergency_mode"],
            "emergency_start_time": self.stats["emergency_start_time"]
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Загружаем цистерны
                self.cisterns = [Cistern.from_dict(c) for c in data.get("cisterns", [])]
                
                # Загружаем статистику
                self.stats.update(data.get("stats", {}))
                
                # Загружаем транзакции
                self.transactions = data.get("transactions", [])
                
                # Восстанавливаем подключения колонок
                self.setup_column_connections()
                
                print("Данные успешно загружены.")
            except Exception as e:
                print(f"Ошибка загрузки данных: {e}. Используются начальные значения.")
    
    def add_transaction(self, trans_type: str, details: str, amount: float = 0.0):
        transaction = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": trans_type,
            "details": details,
            "amount": amount
        }
        self.transactions.append(transaction)
        self.save_data()
    
    def show_header(self):
        print("=" * 50)
        print("АЗС <<СеверНефть>>")
        print("Система управления заправочной станцией")
        print("=" * 50)
        
        # Проверяем отключенные цистерны
        disabled_cisterns = [c for c in self.cisterns if not c.is_enabled]
        if disabled_cisterns and not self.stats["emergency_mode"]:
            print("\nВНИМАНИЕ!")
            print("Обнаружены отключённые цистерны:")
            for cistern in disabled_cisterns:
                print(f" - {cistern.fuel_type} {cistern.id}", end="")
                if cistern.current_volume < cistern.min_level:
                    print(" (низкий уровень топлива)")
                else:
                    print()
    
    def show_main_menu(self):
        while True:
            self.show_header()
            print("\n" + "-" * 40)
            print("Выберите действие:")
            print("1) Обслужить клиента (касса)")
            print("2) Проверить состояние цистерн")
            print("3) Оформить пополнение топлива")
            print("4) Баланс и статистика")
            print("5) История операций")
            print("6) Перекачка топлива между цистернами")
            print("7) Включение / отключение цистерн")
            print("8) Состояние колонок")
            print("9) EMERGENCY - аварийная ситуация")
            print("0) Выход")
            
            if self.stats["emergency_mode"]:
                print("\n!!! АВАРИЙНЫЙ РЕЖИМ !!!")
                emergency_time = self.stats["emergency_start_time"]
                print(f"Активирован: {emergency_time}")
            
            choice = input("\n> ").strip()
            
            if choice == "0":
                self.save_data()
                print("Данные сохранены. До свидания!")
                break
            elif choice == "1":
                self.serve_customer()
            elif choice == "2":
                self.show_cisterns_status()
            elif choice == "3":
                self.refill_fuel()
            elif choice == "4":
                self.show_stats()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                self.transfer_fuel()
            elif choice == "7":
                self.manage_cisterns()
            elif choice == "8":
                self.show_columns_status()
            elif choice == "9":
                self.emergency_procedure()
            else:
                print("Неверный выбор. Попробуйте снова.")
            
            input("\nНажмите Enter для продолжения...")
    
    def serve_customer(self):
        if self.stats["emergency_mode"]:
            print("\n!!! АВАРИЙНЫЙ РЕЖИМ !!!")
            print("Заправка приостановлена. Возобновление работы невозможно до отключения аварийного режима.")
            return
        
        print("\n--- Обслуживание клиента ---")
        
        # Показываем доступные колонки
        print("\nДоступные колонки:")
        for i, column in enumerate(self.columns, 1):
            available_fuels = column.get_available_fuels()
            if available_fuels:
                print(f"{i}) Колонка {i}")
        
        try:
            col_choice = int(input("\nВыберите колонку: ")) - 1
            if not (0 <= col_choice < len(self.columns)):
                print("Неверный номер колонки.")
                return
            
            column = self.columns[col_choice]
            available_fuels = column.get_available_fuels()
            
            if not available_fuels:
                print("На этой колонке нет доступного топлива.")
                return
            
            print(f"\nКолонка {col_choice + 1}")
            print("\nДоступные виды топлива:")
            for i, (fuel_type, cistern) in enumerate(available_fuels, 1):
                print(f"{i}) {fuel_type} (цистерна {cistern.id})")
            
            fuel_choice = int(input("\nВыберите тип топлива: ")) - 1
            if not (0 <= fuel_choice < len(available_fuels)):
                print("Неверный выбор топлива.")
                return
            
            fuel_type, cistern = available_fuels[fuel_choice]
            
            # Проверяем состояние цистерны
            if not cistern.is_enabled:
                print(f"\nОШИБКА:")
                print(f"Цистерна {cistern.id} отключена.")
                print("Отпуск топлива невозможен.")
                return
            
            # Запрашиваем количество
            try:
                liters = float(input("\nВведите количество литров: "))
                if liters <= 0:
                    print("Количество должно быть положительным.")
                    return
                
                # Проверяем достаточно ли топлива
                if not cistern.can_dispense(liters):
                    print("\nОШИБКА: Недостаточно топлива в цистерне.")
                    print(f"Доступно: {cistern.current_volume:.1f} л")
                    return
                
                # Расчет стоимости
                price = PRICES.get(fuel_type, 0)
                cost = liters * price
                
                print(f"\nСтоимость:")
                print(f"{liters:.1f} л × {price:.2f} ₽ = {cost:.2f} ₽")
                
                # Подтверждение
                confirm = input("\nПодтвердить оплату? (y/n): ").lower()
                if confirm == 'y':
                    # Списание топлива
                    success = column.dispense_fuel(fuel_type, liters)
                    if success:
                        # Обновляем статистику
                        self.stats["total_cars"] += 1
                        self.stats["total_income"] += cost
                        self.stats["fuel_sold"][fuel_type] += liters
                        self.stats["fuel_income"][fuel_type] += cost
                        
                        # Добавляем транзакцию
                        self.add_transaction(
                            "продажа",
                            f"Колонка {col_choice+1}: {liters:.1f} л {fuel_type}",
                            cost
                        )
                        
                        print("\nОперация выполнена успешно.")
                        print("Спасибо за покупку!")
                    else:
                        print("\nОшибка при списании топлива.")
                else:
                    print("Операция отменена.")
                    
            except ValueError:
                print("Неверный формат числа.")
                
        except ValueError:
            print("Неверный формат ввода.")
    
    def show_cisterns_status(self):
        print("\n--- Состояние цистерн ---")
        print("\nДоступные цистерны:")
        
        for i, cistern in enumerate(self.cisterns, 1):
            print(f"{i}) {cistern.get_status()}")
    
    def refill_fuel(self):
        if self.stats["emergency_mode"]:
            print("\n!!! АВАРИЙНЫЙ РЕЖИМ !!!")
            print("Пополнение топлива заблокировано.")
            return
        
        print("\n--- Пополнение топлива ---")
        
        # Группируем цистерны по типу топлива
        fuel_groups = {}
        for cistern in self.cisterns:
            if cistern.fuel_type not in fuel_groups:
                fuel_groups[cistern.fuel_type] = []
            fuel_groups[cistern.fuel_type].append(cistern)
        
        print("\nДоступные типы топлива:")
        fuels = list(fuel_groups.keys())
        for i, fuel in enumerate(fuels, 1):
            print(f"{i}) {fuel}")
        
        try:
            fuel_choice = int(input("\nВыберите тип топлива: ")) - 1
            if not (0 <= fuel_choice < len(fuels)):
                print("Неверный выбор.")
                return
            
            fuel_type = fuels[fuel_choice]
            cisterns = fuel_groups[fuel_type]
            
            print(f"\nЦистерны с {fuel_type}:")
            for i, cistern in enumerate(cisterns, 1):
                print(f"{i}) {cistern.id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л")
            
            cistern_choice = int(input("\nВыберите цистерну: ")) - 1
            if not (0 <= cistern_choice < len(cisterns)):
                print("Неверный выбор.")
                return
            
            cistern = cisterns[cistern_choice]
            
            try:
                liters = float(input("\nВведите количество литров для пополнения: "))
                if liters <= 0:
                    print("Количество должно быть положительным.")
                    return
                
                if cistern.current_volume + liters > cistern.max_volume:
                    max_add = cistern.max_volume - cistern.current_volume
                    print(f"\nОШИБКА: Превышение максимального объема.")
                    print(f"Можно добавить максимум: {max_add:.1f} л")
                    return
                
                # Пополняем
                if cistern.refill(liters):
                    # Обновляем статистику
                    self.stats["refills"][fuel_type] += liters
                    
                    # Добавляем транзакцию
                    self.add_transaction(
                        "пополнение",
                        f"{fuel_type} {cistern.id}: +{liters:.1f} л",
                        liters
                    )
                    
                    print(f"\nЦистерна {cistern.id} успешно пополнена на {liters:.1f} л.")
                    print(f"Текущий объем: {cistern.current_volume:.1f} / {cistern.max_volume:.1f} л")
                else:
                    print("Ошибка при пополнении.")
                    
            except ValueError:
                print("Неверный формат числа.")
                
        except ValueError:
            print("Неверный формат ввода.")
    
    def show_stats(self):
        print("\n--- Баланс и статистика ---")
        
        print(f"\nОбслужено автомобилей: {self.stats['total_cars']}")
        print(f"Общий доход: {self.stats['total_income']:,.2f} ₽")
        
        print("\nПродано топлива:")
        for fuel_type in PRICES.keys():
            liters = self.stats["fuel_sold"].get(fuel_type, 0)
            income = self.stats["fuel_income"].get(fuel_type, 0)
            print(f"{fuel_type:6} - {liters:6.0f} л ({income:9,.0f} ₽)")
    
    def show_transaction_history(self):
        print("\n--- История операций ---")
        
        if not self.transactions:
            print("История операций пуста.")
            return
        
        # Показываем последние 20 операций
        recent = self.transactions[-20:]
        for trans in recent:
            print(f"{trans['timestamp']} - {trans['type']}: {trans['details']}", end="")
            if trans['amount'] > 0:
                if trans['type'] == 'продажа':
                    print(f" ({trans['amount']:.2f} ₽)")
                else:
                    print(f" ({trans['amount']:.1f} л)")
            else:
                print()
    
    def transfer_fuel(self):
        if self.stats["emergency_mode"]:
            print("\n!!! АВАРИЙНЫЙ РЕЖИМ !!!")
            print("Перекачка топлива заблокирована.")
            return
        
        print("\n--- Перекачка топлива ---")
        
        # Группируем цистерны по типу топлива
        fuel_groups = {}
        for cistern in self.cisterns:
            if cistern.fuel_type not in fuel_groups:
                fuel_groups[cistern.fuel_type] = []
            fuel_groups[cistern.fuel_type].append(cistern)
        
        # Выбираем тип топлива
        print("\nДоступные типы топлива:")
        fuels = list(fuel_groups.keys())
        for i, fuel in enumerate(fuels, 1):
            print(f"{i}) {fuel}")
        
        try:
            fuel_choice = int(input("\nВыберите тип топлива: ")) - 1
            if not (0 <= fuel_choice < len(fuels)):
                print("Неверный выбор.")
                return
            
            fuel_type = fuels[fuel_choice]
            cisterns = fuel_groups[fuel_type]
            
            if len(cisterns) < 2:
                print(f"Для {fuel_type} доступна только одна цистерна.")
                return
            
            print(f"\nЦистерны с {fuel_type}:")
            for i, cistern in enumerate(cisterns, 1):
                status = "ВКЛ" if cistern.is_enabled else "ВЫКЛ"
                print(f"{i}) {cistern.id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л | {status}")
            
            # Выбираем источник
            source_idx = int(input("\nВыберите цистерну-источник: ")) - 1
            if not (0 <= source_idx < len(cisterns)):
                print("Неверный выбор.")
                return
            
            source = cisterns[source_idx]
            
            # Выбираем приемник
            target_idx = int(input("Выберите цистерну-приемник: ")) - 1
            if not (0 <= target_idx < len(cisterns)):
                print("Неверный выбор.")
                return
            
            if source_idx == target_idx:
                print("Источник и приемник не могут быть одинаковыми.")
                return
            
            target = cisterns[target_idx]
            
            try:
                liters = float(input("\nВведите количество литров для перекачки: "))
                if liters <= 0:
                    print("Количество должно быть положительным.")
                    return
                
                # Проверяем достаточно ли топлива в источнике
                if not source.can_dispense(liters):
                    print(f"\nОШИБКА: В источнике недостаточно топлива.")
                    print(f"Доступно: {source.current_volume:.1f} л")
                    return
                
                # Проверяем вместимость приемника
                if target.current_volume + liters > target.max_volume:
                    max_transfer = target.max_volume - target.current_volume
                    print(f"\nОШИБКА: Приемник не вместит такое количество.")
                    print(f"Максимум можно перекачать: {max_transfer:.1f} л")
                    return
                
                # Выполняем перекачку
                if source.dispense(liters) and target.refill(liters):
                    # Добавляем транзакцию
                    self.add_transaction(
                        "перекачка",
                        f"{fuel_type}: {source.id} -> {target.id}, {liters:.1f} л",
                        liters
                    )
                    
                    print(f"\nПерекачка успешно выполнена.")
                    print(f"Из {source.id}: -{liters:.1f} л (осталось {source.current_volume:.1f} л)")
                    print(f"В {target.id}: +{liters:.1f} л (теперь {target.current_volume:.1f} л)")
                else:
                    print("Ошибка при перекачке.")
                    
            except ValueError:
                print("Неверный формат числа.")
                
        except ValueError:
            print("Неверный формат ввода.")
    
    def manage_cisterns(self):
        if self.stats["emergency_mode"]:
            print("\n!!! АВАРИЙНЫЙ РЕЖИМ !!!")
            print("Управление цистернами заблокировано.")
            return
        
        print("\n--- Управление цистернами ---")
        
        print("\nДоступные действия:")
        print("1) Включить цистерну")
        print("2) Отключить цистерну")
        
        try:
            action = input("\n> ").strip()
            
            if action == "1":
                # Включение цистерн
                disabled = [c for c in self.cisterns if not c.is_enabled]
                
                if not disabled:
                    print("Нет отключенных цистерн.")
                    return
                
                print("\nЦистерны, доступные для включения:")
                for i, cistern in enumerate(disabled, 1):
                    print(f"{i}) {cistern.fuel_type} {cistern.id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л")
                
                choice = int(input("\nВыберите цистерну: ")) - 1
                if not (0 <= choice < len(disabled)):
                    print("Неверный выбор.")
                    return
                
                cistern = disabled[choice]
                cistern.is_enabled = True
                
                # Добавляем транзакцию
                self.add_transaction(
                    "включение",
                    f"{cistern.fuel_type} {cistern.id}"
                )
                
                print(f"\nЦистерна {cistern.id} успешно включена.")
                
            elif action == "2":
                # Отключение цистерн
                enabled = [c for c in self.cisterns if c.is_enabled]
                
                if not enabled:
                    print("Нет включенных цистерн.")
                    return
                
                print("\nЦистерны, доступные для отключения:")
                for i, cistern in enumerate(enabled, 1):
                    print(f"{i}) {cistern.fuel_type} {cistern.id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л")
                
                choice = int(input("\nВыберите цистерну: ")) - 1
                if not (0 <= choice < len(enabled)):
                    print("Неверный выбор.")
                    return
                
                cistern = enabled[choice]
                cistern.is_enabled = False
                
                # Добавляем транзакцию
                self.add_transaction(
                    "отключение",
                    f"{cistern.fuel_type} {cistern.id}"
                )
                
                print(f"\nЦистерна {cistern.id} успешно отключена.")
                
            else:
                print("Неверный выбор.")
                
        except ValueError:
            print("Неверный формат ввода.")
    
    def show_columns_status(self):
        print("\n--- Состояние колонок ---")
        
        for column in self.columns:
            print(f"\nКолонка {column.column_id}:")
            
            for fuel_type, cistern in column.fuel_connections.items():
                status = "✓" if cistern.is_enabled else "✗"
                status_desc = "работает" if cistern.is_enabled else "не работает"
                print(f"  {fuel_type}: цистерна {cistern.id} [{status}] {status_desc}")
    
    def emergency_procedure(self):
        print("\n=== EMERGENCY - АВАРИЙНАЯ СИТУАЦИЯ ===")
        
        if self.stats["emergency_mode"]:
            print("\nТекущий статус: АВАРИЙНЫЙ РЕЖИМ АКТИВЕН")
            print("Доступные действия:")
            print("1) Отключить аварийный режим")
            print("2) Вернуться в меню")
            
            choice = input("\n> ").strip()
            
            if choice == "1":
                confirm = input("\nВы уверены, что хотите отключить аварийный режим? (y/n): ").lower()
                if confirm == 'y':
                    self.stats["emergency_mode"] = False
                    self.stats["emergency_start_time"] = None
                    
                    # Добавляем транзакцию
                    self.add_transaction(
                        "авария",
                        "Отключение аварийного режима"
                    )
                    
                    print("\nАварийный режим отключен.")
                    print("ВНИМАНИЕ: Цистерны остаются заблокированными!")
                    print("Разблокируйте их вручную через меню управления цистернами.")
                else:
                    print("Отмена.")
            return
        
        print("\nВНИМАНИЕ: Активация аварийного режима приведет к:")
        print("1) Блокировке ВСЕХ цистерн")
        print("2) Прекращению заправки")
        print("3) Фиксации аварийного события")
        print("4) Имитации вызова аварийных служб")
        
        confirm = input("\nВы уверены, что хотите активировать аварийный режим? (y/n): ").lower()
        
        if confirm == 'y':
            # Активируем аварийный режим
            self.stats["emergency_mode"] = True
            self.stats["emergency_start_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Блокируем все цистерны
            for cistern in self.cisterns:
                cistern.is_enabled = False
            
            # Добавляем транзакцию
            self.add_transaction(
                "авария",
                "Активация аварийного режима"
            )
            
            print("\n" + "!" * 50)
            print("АВАРИЙНЫЙ РЕЖИМ АКТИВИРОВАН!")
            print("!" * 50)
            print("\nВсе цистерны заблокированы.")
            print("Заправка прекращена.")
            print("Имитация вызова аварийных служб...")
            print("Службы уведомлены. Ожидайте прибытия.")
        else:
            print("Отмена.")

def main():
    system = AZSSystem()
    system.show_main_menu()

if __name__ == "__main__":
    main()