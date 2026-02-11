---
title: ""
author: ""
date: ""
---

<div align="center">

МИНОБРНАУКИ РОССИИ  

Федеральное государственное бюджетное образовательное учреждение высшего образования  

«ВЛАДИВОСТОКСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»

Институт информационных технологий и анализа данных  
Кафедра информационных технологий и систем  

<br><br><br>

# ОТЧЁТ  
## ПО РАЗРАБОТКЕ СИСТЕМЫ УПРАВЛЕНИЯ  
## АВТОЗАПРАВОЧНОЙ СТАНЦИЕЙ НА PYTHON  

<br><br>

Студент: С.А. Головцов  
Группа: ___________________  

Преподаватель: ___________________  

<br><br><br><br>

Владивосток 2026

</div>

\newpage

# СОДЕРЖАНИЕ

1 Задание  
2 Выполнение работы  
&nbsp;&nbsp;&nbsp;2.1 Общая структура программы  
&nbsp;&nbsp;&nbsp;2.2 Класс Cistern  
&nbsp;&nbsp;&nbsp;2.3 Класс FuelColumn  
&nbsp;&nbsp;&nbsp;2.4 Класс AZSSystem  
&nbsp;&nbsp;&nbsp;2.5 Основной запуск программы  
3 Заключение  

\newpage

# 1 ЗАДАНИЕ

Разработать систему управления автозаправочной станцией на языке Python.  
Система должна обеспечивать хранение топлива, отпуск через колонки, ведение статистики, обработку аварийного режима и сохранение данных.

\newpage

# 2 ВЫПОЛНЕНИЕ РАБОТЫ

## 2.1 Общая структура программы
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

DATA_FILE = "azs_data.json"

PRICES = {
    "АИ-92": 57.50,
    "АИ-95": 58.30,
    "АИ-98": 64.20,
    "ДТ": 56.80
}

Листинг 2.1 – Импорт библиотек и глобальные параметры  

---

## 2.2 Класс Cistern
class Cistern:
    def __init__(self, fuel_type: str, max_volume: float, min_level_percent: float = 10.0):
        self.fuel_type = fuel_type
        self.max_volume = max_volume
        self.current_volume = max_volume * 0.5
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

Листинг 2.2 – Реализация класса Cistern  

---

## 2.3 Класс FuelColumn
class FuelColumn:
    def __init__(self, column_id: int):
        self.column_id = column_id
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

Степа, [11.02.2026 23:41]
if fuel_type in self.fuel_connections:
            cistern = self.fuel_connections[fuel_type]
            if cistern.dispense(amount):
                return amount * PRICES.get(fuel_type, 0)
        return None

Листинг 2.3 – Реализация класса FuelColumn
## 2.4 Класс AZSSystem
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
        
        for i in range(1, 9):
            column = FuelColumn(i)
            self.columns.append(column)
        
        self.setup_column_connections()

Листинг 2.4 – Начало реализации класса AZSSystem  
Степа, [11.02.2026 23:44]
def setup_column_connections(self):
        for column in self.columns:
            for cistern in self.cisterns:
                column.connect_fuel(cistern.fuel_type, cistern)

    def save_data(self):
        data = {
            "cisterns": [c.to_dict() for c in self.cisterns],
            "stats": self.stats
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.cisterns = [Cistern.from_dict(c) for c in data["cisterns"]]
                self.stats = data["stats"]

    def refuel_car(self, column_id: int, fuel_type: str, amount: float):
        column = self.columns[column_id - 1]
        payment = column.dispense_fuel(fuel_type, amount)
        
        if payment is not None:
            self.stats["total_cars"] += 1
            self.stats["total_income"] += payment
            self.stats["fuel_sold"][fuel_type] += amount
            self.stats["fuel_income"][fuel_type] += payment
            
            self.transactions.append({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "column": column_id,
                "fuel": fuel_type,
                "amount": amount,
                "payment": payment
            })
            return payment
        return None

    def show_statistics(self):
        print("\n--- Статистика ---")
        print(f"Обслужено автомобилей: {self.stats['total_cars']}")
        print(f"Общий доход: {self.stats['total_income']:.2f} руб.")
        for fuel in PRICES:
            print(f"{fuel}: продано {self.stats['fuel_sold'][fuel]:.2f} л, "
                  f"доход {self.stats['fuel_income'][fuel]:.2f} руб.")

    def toggle_emergency(self):
        self.stats["emergency_mode"] = not self.stats["emergency_mode"]
        if self.stats["emergency_mode"]:
            self.stats["emergency_start_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Аварийный режим включен.")
        else:
            print("Аварийный режим отключен.")
            self.stats["emergency_start_time"] = None

    def show_main_menu(self):
        while True:
            print("\n1. Заправить автомобиль")
            print("2. Показать статистику")
            print("3. Аварийный режим")
            print("4. Сохранить данные")
            print("0. Выход")
            
            choice = input("Выберите пункт: ")
            
            if choice == "1":
                column_id = int(input("Номер колонки: "))
                fuel_type = input("Тип топлива: ")
                amount = float(input("Количество литров: "))
                payment = self.refuel_car(column_id, fuel_type, amount)
                if payment:
                    print(f"К оплате: {payment:.2f} руб.")
                else:
                    print("Ошибка операции.")
            
            elif choice == "2":
                self.show_statistics()
            
            elif choice == "3":
                self.toggle_emergency()
            
            elif choice == "4":
                self.save_data()
                print("Данные сохранены.")
            
            elif choice == "0":
                self.save_data()
                break
            
            else:
                print("Неверный ввод.")

Листинг 2.5 – Продолжение реализации класса AZSSystem  

---

## 2.5 Основной запуск программы
def main():
    system = AZSSystem()
    system.show_main_menu()

if __name__ == "__main__":
    main()

Листинг 2.6 – Точка входа в программу  

---

# 3 ЗАКЛЮЧЕНИЕ

В ходе выполнения работы была разработана программная система управления автозаправочной станцией на языке Python.  

Реализована объектно-ориентированная архитектура, включающая классы для хранения топлива, управления колонками, ведения статистики и обработки аварийного режима.

Степа, [11.02.2026 23:44]
Программа обеспечивает моделирование работы АЗС, позволяет сохранять данные в файл и восстанавливать состояние системы при повторном запуске.  

Разработанная система демонстрирует практическое применение языка Python для решения прикладных задач автоматизации.