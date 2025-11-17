print('task 1:')

name = input('Введите имя:')
age = int(input('Введите возраст:'))
for i in range(10):
     print(f'Меня зовут {name}, мне {age} лет.')


print('task 2:')
number = int(input('Введите число от 1 до 9:'))

if 1<= number <= 9:
    print(f"Таблица умножения для числа {number}:")

    for i in range(1,11):
        result = number * i
        print(f"{number} * {i} = {result}")
else:
    print("Ошибка! Введите число от 1 до 9.")


print('task 3:')
iMin = 0
iMax = 100
for i in range(iMin+2, iMax+1, 3):
    print(i)


print('task 4:')

t = int(input("Введите число: "))

factorial = 1
for i in range(1, t + 1):
    factorial *= i

print(f"Факториал числа {t} равен {factorial} ")


print('task 5:')

i = 20
while i >= 0:
    print(i)
    i -= 1


print('task 6:')

k = int(input("Введите число: "))

a, b = 0, 1
print("Числа Фибоначчи до", k,":" )

while a <= k:
    print(a, end=' ')
    a, b = b, a + b


print('task 7:')

word = input("Введите слово: ")

result = ""
for i, char in enumerate(word):
    result += f"{char}{i + 1}"

print("Новая строка:", result)


print('task 8:')

flag = True

while flag:
    print('Введите два числа через пробел:')
    a, b = input().split(' ')
    print(f'Сумма чисел равна: {int(a) + int(b)}')