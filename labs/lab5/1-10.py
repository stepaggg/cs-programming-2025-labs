print("=== ЗАДАНИЕ 1 ===")
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers1)):
    if numbers1[i] == 3:
        numbers1[i] = 30
print(numbers1)

print("\n=== ЗАДАНИЕ 2 ===")
numbers2 = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers2]
print(squares)

print("\n=== ЗАДАНИЕ 3 ===")
numbers3 = [10, 20, 30, 40]
max_num = max(numbers3)
result = max_num / len(numbers3)
print(result)

print("\n=== ЗАДАНИЕ 4 ===")
t = (3, 1, 4, 2)
try:
    result_t = tuple(sorted(t))
except:
    result_t = t
print(result_t)

print("\n=== ЗАДАНИЕ 5 ===")
products = {"хлеб": 30, "молоко": 80, "сыр": 200}
min_product = min(products, key=products.get)
max_product = max(products, key=products.get)
print(f"Минимум: {min_product}")
print(f"Максимум: {max_product}")

print("\n=== ЗАДАНИЕ 6 ===")
items = ["a", "b", "c"]
d = {}
for item in items:
    d[item] = item
print(d)

print("\n=== ЗАДАНИЕ 7 ===")
eng_rus = {"apple": "яблоко", "cat": "кот"}
rus_eng = {}
for eng, rus in eng_rus.items():
    rus_eng[rus] = eng
word = "яблоко"
if word in rus_eng:
    print(f"Перевод: {rus_eng[word]}")

print("\n=== ЗАДАНИЕ 8 ===")
import random
rules = {
    "камень": ["ножницы", "ящерица"],
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "спок"],
    "ящерица": ["бумага", "спок"],
    "спок": ["камень", "ножницы"]
}
choices = list(rules.keys())
user = "камень"
comp = random.choice(choices)
print(f"Вы: {user}, Компьютер: {comp}")
if user == comp:
    print("Ничья")
elif comp in rules[user]:
    print("Вы выиграли")
else:
    print("Компьютер выиграл")

print("\n=== ЗАДАНИЕ 9 ===")
words = ["яблоко", "груша", "банан", "киви", "ананас"]
result_dict = {}
for word in words:
    letter = word[0]
    if letter not in result_dict:
        result_dict[letter] = []
    result_dict[letter].append(word)
print(result_dict)

print("\n=== ЗАДАНИЕ 10 ===")
students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
averages = {}
for name, grades in students:
    avg = sum(grades) / len(grades)
    averages[name] = avg
best_name = max(averages, key=averages.get)
best_avg = averages[best_name]
print(f"Лучший: {best_name} - {best_avg}")