from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
import subprocess

def open_file_in_word(filename):
    """Автоматическое открытие файла в Word"""
    try:
        if os.name == 'nt':  # Windows
            os.startfile(filename)
        else:  # Mac или Linux
            subprocess.call(['open', filename])
        print(f"✓ Открываю файл: {filename}")
    except Exception as e:
        print(f"✗ Не удалось открыть файл автоматически: {e}")

def create_compact_report():
    """Создание КРАТКОГО отчета (5 страниц)"""
    
    doc = Document()
    
    # Настройка стилей
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)  # Меньше шрифт для компактности
    
    # Настройка страницы
    section = doc.sections[0]
    section.page_height = Inches(11.7)
    section.page_width = Inches(8.3)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(0.8)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    
    # ===== ТИТУЛЬНЫЙ ЛИСТ =====
    print("Создаю титульный лист...")
    
    for _ in range(6):
        doc.add_paragraph()
    
    # Заголовки
    headers = [
        ("МИНОБРНАУКИ РОССИИ", True),
        ("Федеральное государственное бюджетное", False),
        ("образовательное учреждение высшего образования", False),
        ("«ВЛАДИВОСТОКСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»", True),
        ("(ФГБОУ ВО «ВВГУ»)", False),
        ("", False),
        ("ИНСТИТУТ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И АНАЛИЗА ДАННЫХ", True),
        ("КАФЕДРА ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И СИСТЕМ", True),
    ]
    
    for text, bold in headers:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if text:
            run = p.add_run(text)
            run.font.size = Pt(12)
            run.bold = bold
    
    for _ in range(4):
        doc.add_paragraph()
    
    # Название работы
    work_headers = [
        ("ОТЧЕТ", True, 14),
        ("ПО ЛАБОРАТОРНОЙ РАБОТЕ №1", True, 12),
        ("по дисциплине", False, 12),
        ("«Информатика и программирование»", True, 12),
    ]
    
    for text, bold, size in work_headers:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.bold = bold
    
    for _ in range(6):
        doc.add_paragraph()
    
    # Данные студента
    student_info = [
        "Студент",
        "гр. БИН-25-2", 
        "Ассистент",
        "преподавателя"
    ]
    
    for text in student_info:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(text)
        run.font.size = Pt(12)
    
    for _ in range(2):
        doc.add_paragraph()
    
    # Подписи
    signatures = [
        "_________________________",
        "С.А. Головцов",
        "_________________________",
        "М.В. Водяницкий"
    ]
    
    for text in signatures:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(text)
        run.font.size = Pt(12)
    
    for _ in range(8):
        doc.add_paragraph()
    
    # Город и год
    p_city = doc.add_paragraph()
    p_city.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_city = p_city.add_run("Владивосток 2025")
    run_city.font.size = Pt(12)
    run_city.bold = True
    
    # ===== КРАТКОЕ СОДЕРЖАНИЕ =====
    doc.add_page_break()
    
    p_content = doc.add_paragraph()
    p_content.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_content = p_content.add_run("СОДЕРЖАНИЕ")
    run_content.font.size = Pt(14)
    run_content.bold = True
    
    doc.add_paragraph()
    
    content_items = [
        "1. Введение................................................2",
        "2. Задание 1: Управление кондиционером....................3",
        "3. Задание 2: Определение времени года....................3", 
        "4. Задание 3: Расчет возраста собаки......................3",
        "5. Задание 4: Проверка делимости на 6.....................4",
        "6. Задание 5: Проверка надежности пароля..................4",
        "7. Задание 6: Определение високосного года................4",
        "8. Задание 7: Поиск наименьшего числа.....................5",
        "9. Задание 8: Расчет скидки в магазине....................5",
        "10. Задание 9: Определение времени суток..................5",
        "11. Задание 10: Проверка простого числа...................5"
    ]
    
    for item in content_items:
        p = doc.add_paragraph(item)
        p.style = doc.styles['Normal']
    
    # ===== КРАТКОЕ ВВЕДЕНИЕ =====
    doc.add_page_break()
    
    p_intro = doc.add_paragraph()
    p_intro.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_intro = p_intro.add_run("1. ВВЕДЕНИЕ")
    run_intro.font.size = Pt(14)
    run_intro.bold = True
    
    doc.add_paragraph()
    
    intro_text = [
        "Цель: освоение базовых конструкций Python и условных операторов.",
        "",
        "Задачи:",
        "• Разработка 10 практических задач",
        "• Изучение условных операторов if-else", 
        "• Работа с пользовательским вводом",
        "",
        "Технологии: Python 3.x, стандартные библиотеки."
    ]
    
    for text in intro_text:
        p = doc.add_paragraph(text)
        p.paragraph_format.line_spacing = 1.0
    
    # ===== КОМПАКТНЫЕ ЗАДАНИЯ =====
    doc.add_page_break()
    
    # Группируем задания по 2 на страницу
    compact_tasks = [
        {
            "number": "2",
            "title": "Управление кондиционером",
            "code": '''temp = float(input("Температура: "))
print("Выключен" if temp >= 20 else "Включен")''',
            "explanation": "Кондиционер включается при температуре ниже 20°C"
        },
        {
            "number": "3", 
            "title": "Определение времени года",
            "code": '''month = int(input("Месяц: "))
if month in [12,1,2]: print("Зима")
elif month in [3,4,5]: print("Весна") 
elif month in [6,7,8]: print("Лето")
else: print("Осень")''',
            "explanation": "Определение сезона по номеру месяца"
        },
        {
            "number": "4",
            "title": "Расчет возраста собаки",
            "code": '''age = float(input("Возраст собаки: "))
if age <= 2: result = age * 10.5
else: result = 21 + (age - 2) * 4
print(f"Человеческих лет: {result}")''',
            "explanation": "Первые 2 года = 10.5 чел.лет, далее = 4 чел.года"
        },
        {
            "number": "5",
            "title": "Проверка делимости на 6", 
            "code": '''num = input("Число: ")
last = int(num[-1])
total = sum(int(d) for d in num)
if last % 2 == 0 and total % 3 == 0:
    print("Делится на 6")''',
            "explanation": "Делится если: четное И сумма цифр делится на 3"
        },
        {
            "number": "6",
            "title": "Проверка надежности пароля",
            "code": '''pwd = input("Пароль: ")
errors = []
if len(pwd) < 8: errors.append("короткий")
if not any(c.isupper() for c in pwd): errors.append("нет заглавных")
if not any(c.islower() for c in pwd): errors.append("нет строчных") 
if not any(c.isdigit() for c in pwd): errors.append("нет цифр")
if pwd.isalnum(): errors.append("нет спецсимволов")
print("Надежный" if not errors else "Ненадежный")''',
            "explanation": "Проверка 5 критериев надежности пароля"
        }
    ]
    
    # Добавляем первые 5 заданий на одну страницу
    print("Создаю компактные задания...")
    
    for task in compact_tasks:
        # Заголовок задания
        p_title = doc.add_paragraph()
        run_title = p_title.add_run(f"{task['number']}. {task['title']}")
        run_title.font.size = Pt(12)
        run_title.bold = True
        
        # Код (компактный)
        p_code = doc.add_paragraph(task['code'])
        p_code.style = doc.styles['Normal']
        
        # Объяснение
        p_expl = doc.add_paragraph(task['explanation'])
        p_expl.style = doc.styles['Normal']
        
        doc.add_paragraph()  # Маленький отступ между заданиями
    
    # ===== ВТОРАЯ СТРАНИЦА С ЗАДАНИЯМИ =====
    doc.add_page_break()
    
    more_compact_tasks = [
        {
            "number": "7",
            "title": "Определение високосного года",
            "code": '''year = int(input("Год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Високосный")''',
            "explanation": "Високосный если: (делится на 4 И не на 100) ИЛИ делится на 400"
        },
        {
            "number": "8", 
            "title": "Поиск наименьшего числа",
            "code": '''a, b, c = map(float, input("3 числа: ").split())
min_num = a
if b < min_num: min_num = b
if c < min_num: min_num = c
print(f"Наименьшее: {min_num}")''',
            "explanation": "Последовательное сравнение трех чисел"
        },
        {
            "number": "9",
            "title": "Расчет скидки в магазине",
            "code": '''amount = float(input("Сумма: "))
if amount < 1000: discount = 0
elif amount <= 5000: discount = 5
elif amount <= 10000: discount = 10
else: discount = 15
print(f"Скидка: {discount}%")''',
            "explanation": "Скидки: 0-5-10-15% в зависимости от суммы"
        },
        {
            "number": "10",
            "title": "Определение времени суток", 
            "code": '''hour = int(input("Час: "))
if 0 <= hour <= 5: print("Ночь")
elif 6 <= hour <= 11: print("Утро")
elif 12 <= hour <= 17: print("День")
else: print("Вечер")''',
            "explanation": "Ночь:0-5, Утро:6-11, День:12-17, Вечер:18-23"
        },
        {
            "number": "11",
            "title": "Проверка простого числа",
            "code": '''num = int(input("Число: "))
if num < 2: print("Не простое")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            print("Составное")
            break
    else: print("Простое")''',
            "explanation": "Простое число делится только на 1 и себя"
        }
    ]
    
    # Добавляем остальные задания
    for task in more_compact_tasks:
        p_title = doc.add_paragraph()
        run_title = p_title.add_run(f"{task['number']}. {task['title']}")
        run_title.font.size = Pt(12)
        run_title.bold = True
        
        p_code = doc.add_paragraph(task['code'])
        p_code.style = doc.styles['Normal']
        
        p_expl = doc.add_paragraph(task['explanation'])
        p_expl.style = doc.styles['Normal']
        
        doc.add_paragraph()
    
    # Сохраняем компактный документ
    filename = "КРАТКИЙ_ОТЧЕТ_5_СТРАНИЦ.docx"
    doc.save(filename)
    
    print(f"✓ Краткий отчет создан: {filename}")
    return filename

def install_requirements():
    """Инструкция по установке библиотек"""
    print("\nДля установки библиотеки выполните:")
    print("pip install python-docx")

if __name__ == "__main__":
    try:
        print("Создание КРАТКОГО отчета (5 страниц)...")
        filename = create_compact_report()
        
        print(f"✓ Готово! Файл: {filename}")
        print(f"✓ Путь: {os.path.abspath(filename)}")
        
        # Открываем файл
        open_file_in_word(filename)
        
    except ImportError:
        print("✗ Библиотека python-docx не установлена!")
        install_requirements()
    except Exception as e:
        print(f"✗ Ошибка: {e}")