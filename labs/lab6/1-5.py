
# ========== ЗАДАНИЕ 1 ==========
def time_converter(value, from_unit, to_unit):
    # Переводим всё в секунды
    if from_unit == "h":
        seconds = value * 3600
    elif from_unit == "m":
        seconds = value * 60
    else:  # "s"
        seconds = value
    
    # Переводим из секунд в нужную единицу
    if to_unit == "h":
        return f"{seconds / 3600}h"
    elif to_unit == "m":
        return f"{seconds / 60}m"
    else:  # "s"
        return f"{seconds}s"

# ========== ЗАДАНИЕ 2 ==========
def bank_profit(money, years):
    if money < 30000:
        return "Ошибка: минимальный вклад 30000 рублей"
    
    # Ставка от суммы
    extra = (money // 10000) * 0.003
    if extra > 0.05:
        extra = 0.05
    base_rate = 0.03 + extra
    
    # Ставка от срока
    if years <= 3:
        term_rate = 0.03
    elif 4 <= years <= 6:
        term_rate = 0.05
    else:
        term_rate = 0.02
    
    total_rate = base_rate + term_rate
    
    # Считаем сложный процент
    total = money
    for _ in range(years):
        total = total * (1 + total_rate)
    
    profit = total - money
    return round(profit, 2)

# ========== ЗАДАНИЕ 3 ==========
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    if start > end:
        return "Error!"
    
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    
    if not primes:
        return "Error!"
    
    return " ".join(map(str, primes))

# ========== ЗАДАНИЕ 4 ==========
def add_matrices():
    try:
        n = int(input("Введите размер матрицы: "))
        if n <= 2:
            return "Error!"
        
        print("Введите первую матрицу (по строкам):")
        matrix1 = []
        for _ in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                return "Error!"
            matrix1.append(row)
        
        print("Введите вторую матрицу (по строкам):")
        matrix2 = []
        for _ in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                return "Error!"
            matrix2.append(row)
        
        # Складываем матрицы
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        
        # Выводим результат
        print("Результат:")
        for row in result:
            print(" ".join(map(str, row)))
        return ""
        
    except:
        return "Error!"

# ========== ЗАДАНИЕ 5 ==========
def check_palindrome(text):
    # Очищаем строку
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char.lower()
    
    # Проверяем на палиндром
    if cleaned == cleaned[::-1]:
        return "Да"
    else:
        return "Нет"
