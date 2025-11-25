print('задание 1:')
temp = int(input('введите температуру:'))
def task1():
    print("Кондиционер выключен" if temp >= 20 else "Кондиционер включен")
task1()

# Задание 2: Сезоны года
print('задание 2:')
month = int(input("Введите номер месяца: "))
def task2():
    if month in [12, 1, 2]:
        print("Это зима")
    elif month in [3, 4, 5]:
        print("Это весна")
    elif month in [6, 7, 8]:
        print("Это лето")
    else:
        print("Это осень")
task2()

# Задание 3: Возраст собаки
print('задание 3:')
age = float(input("Введите возраст собаки: "))
def task3():
    if age <= 2:
        result = age * 10.5
    else:
        result = 21 + (age - 2) * 4
    print(f"Возраст в человеческих годах: {result}")
task3()

# Задание 4: Деление на 6
print('задание 4:')
num = input("Введите число: ")
def task4():
    last_digit = int(num[-1])
    digit_sum = sum(int(d) for d in num)
    
    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        print("Делится на 6")
    else:
        print("Не делится на 6")
task4()

# Задание 5: Проверка пароля
print('задание 5:')
pwd = input("Введите пароль: ")
errors = []
def task5():
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
        print("Пароль ненадежный:", ", ",errors)
    else:
        print("Пароль надежный")
task5()

# Задание 6: Високосный год
print('задание 6:')
year = int(input("Введите год: "))
def task6():
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} - високосный")
    else:
        print(f"{year} - невисокосный")
task6()

# Задание 7: Наименьшее число
print('задание 7:')
a, b, c = map(float, input("Введите три числа: ").split())
def task7():
    min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    print(f"Наименьшее: {min_num}")
task7()

# Задание 8: Скидка в магазине
print('задание 8:')
amount = float(input("Введите сумму покупки: "))
def task8():
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
task8()

# Задание 9: Время суток
print('задание 9:')
hour = int(input("Введите час (0-23): "))
def task9():
    if 0 <= hour <= 5:
        print("Ночь")
    elif 6 <= hour <= 11:
        print("Утро")
    elif 12 <= hour <= 17:
        print("День")
    else:
        print("Вечер")
task9()

# Задание 10: Простое число
num = int(input("Введите число: "))
def task10():
    if num < 2:
        print("Не простое")
        return
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} - составное")
            return
    print(f"{num} - простое")
task10()
