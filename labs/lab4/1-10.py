print('задание 1:')
def task1():
    temp = float(input("Введите температуру: "))
    print("Кондиционер выключен" if temp >= 20 else "Кондиционер включен")

# Задание 2: Сезоны года
print('задание 2:')
def task2():
    month = int(input("Введите номер месяца: "))
    if month in [12, 1, 2]:
        print("Это зима")
    elif month in [3, 4, 5]:
        print("Это весна")
    elif month in [6, 7, 8]:
        print("Это лето")
    else:
        print("Это осень")

# Задание 3: Возраст собаки
print('задание 3:')
def task3():
    age = float(input("Введите возраст собаки: "))
    if age <= 2:
        result = age * 10.5
    else:
        result = 21 + (age - 2) * 4
    print(f"Возраст в человеческих годах: {result}")

# Задание 4: Деление на 6
print('задание 4:')
def task4():
    num = input("Введите число: ")
    last_digit = int(num[-1])
    digit_sum = sum(int(d) for d in num)
    
    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        print("Делится на 6")
    else:
        print("Не делится на 6")

# Задание 5: Проверка пароля
print('задание 5:')
def task5():
    pwd = input("Введите пароль: ")
    errors = []
    
    if len(pwd) < 8:
        errors.append("длина менее 8 символов")
    if not any(c.isupper() for c in pwd):
        errors.append("нет заглавных букв")
    if not any(c.islower() for c in pwd):
        errors.append("нет строчных букв")
    if not any(c.isdigit() for c in pwd):
        errors.append("нет цифр")
    if pwd.isalnum():
        errors.append("нет спецсимволов")
    
    if errors:
        print("Пароль ненадежный:", ", ".join(errors))
    else:
        print("Пароль надежный")

# Задание 6: Високосный год
print('задание 6:')
def task6():
    year = int(input("Введите год: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} - високосный")
    else:
        print(f"{year} - невисокосный")

# Задание 7: Наименьшее число
print('задание 7:')
def task7():
    a, b, c = map(float, input("Введите три числа: ").split())
    min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    print(f"Наименьшее: {min_num}")

# Задание 8: Скидка в магазине
print('задание 8:')
def task8():
    amount = float(input("Введите сумму покупки: "))
    if amount < 1000:
        discount = 0
    elif amount <= 5000:
        discount = 5
    elif amount <= 10000:
        discount = 10
    else:
        discount = 15
    
    total = amount * (1 - discount / 100)
    print(f"Скидка: {discount}%")
    print(f"К оплате: {total}")

# Задание 9: Время суток
print('задание 9:')
def task9():
    hour = int(input("Введите час (0-23): "))
    if 0 <= hour <= 5:
        print("Ночь")
    elif 6 <= hour <= 11:
        print("Утро")
    elif 12 <= hour <= 17:
        print("День")
    else:
        print("Вечер")

# Задание 10: Простое число
print('задание 10:')
def task10():
    num = int(input("Введите число: "))
    if num < 2:
        print("Не простое")
        return
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} - составное")
            return
    print(f"{num} - простое")