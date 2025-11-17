
from  docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import os

def create_lab_report_docx():
    """Создание документа Word с титульным листом лабораторной работы"""
    
    # Создаем новый документ
    doc = Document()
    
    # Настройка стилей документа
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    
    # Настройка страницы
    section = doc.sections[0]
    section.page_height = Inches(11.7)  # A4
    section.page_width = Inches(8.3)
    section.top_margin = Inches(1.2)
    section.bottom_margin = Inches(1.2)
    section.left_margin = Inches(1.5)   # 30 мм
    section.right_margin = Inches(0.8)  # 20 мм
    
    # Пустые строки для центрирования по вертикали
    for _ in range(8):
        doc.add_paragraph()
    
    # МИНОБРНАУКИ РОССИИ
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run1 = p1.add_run("МИНОБРНАУКИ РОССИИ")
    run1.font.size = Pt(14)
    run1.font.bold = True
    
    # Федеральное государственное...
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run("Федеральное государственное бюджетное")
    run2.font.size = Pt(14)
    
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run3 = p3.add_run("образовательное учреждение высшего образования")
    run3.font.size = Pt(14)
    
    # ВГУ в кавычках
    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run4 = p4.add_run("«ВЛАДИВОСТОКСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»")
    run4.font.size = Pt(14)
    run4.font.bold = True
    
    # ФГБОУ ВО ВВГУ
    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run5 = p5.add_run("(ФГБОУ ВО «ВВГУ»)")
    run5.font.size = Pt(14)
    
    # Пустые строки
    for _ in range(2):
        doc.add_paragraph()
    
    # Институт
    p6 = doc.add_paragraph()
    p6.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run6 = p6.add_run("ИНСТИТУТ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И АНАЛИЗА ДАННЫХ")
    run6.font.size = Pt(14)
    run6.font.bold = True
    
    # Кафедра
    p7 = doc.add_paragraph()
    p7.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run7 = p7.add_run("КАФЕДРА ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И СИСТЕМ")
    run7.font.size = Pt(14)
    run7.font.bold = True
    
    # Большой отступ перед ОТЧЕТ
    for _ in range(8):
        doc.add_paragraph()
    
    # ОТЧЕТ
    p8 = doc.add_paragraph()
    p8.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run8 = p8.add_run("ОТЧЕТ")
    run8.font.size = Pt(16)
    run8.font.bold = True
    
    # ПО ЛАБОРАТОРНОЙ РАБОТЕ
    p9 = doc.add_paragraph()
    p9.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run9 = p9.add_run("ПО ЛАБОРАТОРНОЙ РАБОТЕ №1")
    run9.font.size = Pt(14)
    run9.font.bold = True
    
    # по дисциплине
    p10 = doc.add_paragraph()
    p10.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run10 = p10.add_run("по дисциплине")
    run10.font.size = Pt(14)
    
    # Название дисциплины
    p11 = doc.add_paragraph()
    p11.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run11 = p11.add_run("«Информатика и программирование»")
    run11.font.size = Pt(14)
    run11.font.bold = True
    
    # Отступ перед данными студента
    for _ in range(10):
        doc.add_paragraph()
    
    # Студент
    p12 = doc.add_paragraph()
    p12.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run12 = p12.add_run("Студент")
    run12.font.size = Pt(14)
    
    # Группа
    p13 = doc.add_paragraph()
    p13.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run13 = p13.add_run("гр. BDI-BDZ-21")
    run13.font.size = Pt(14)
    
    # Ассистент
    p14 = doc.add_paragraph()
    p14.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run14 = p14.add_run("Ассистент")
    run14.font.size = Pt(14)
    
    # преподавателя
    p15 = doc.add_paragraph()
    p15.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run15 = p15.add_run("преподавателя")
    run15.font.size = Pt(14)
    
    # Отступ для подписей
    for _ in range(4):
        doc.add_paragraph()
    
    # Подпись студента
    p16 = doc.add_paragraph()
    p16.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run16 = p16.add_run("_________________________")
    run16.font.size = Pt(14)
    
    # ФИО студента
    p17 = doc.add_paragraph()
    p17.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run17 = p17.add_run("С.А.Головцов")
    run17.font.size = Pt(14)
    
    # Подпись преподавателя
    p18 = doc.add_paragraph()
    p18.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run18 = p18.add_run("_________________________")
    run18.font.size = Pt(14)
    
    # ФИО преподавателя
    p19 = doc.add_paragraph()
    p19.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run19 = p19.add_run("М.В. Водяницкий")
    run19.font.size = Pt(14)
    
    # Отступ перед городом и годом
    for _ in range(12):
        doc.add_paragraph()
    
    # Город и год
    p20 = doc.add_paragraph()
    p20.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run20 = p20.add_run("Владивосток 2025")
    run20.font.size = Pt(14)
    
    # Сохраняем документ
    filename = "Лабораторная_работа_1_титульный_лист.docx"
    doc.save(filename)
    
    print(f"Документ успешно создан: {filename}")
    print(f"Путь: {os.path.abspath(filename)}")
    
    return filename

def create_full_lab_report():
    """Создание полного отчета с титульным листом и содержанием"""
    
    doc = Document()
    
    # Настройка стилей
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    
    # Настройка страницы
    section = doc.sections[0]
    section.page_height = Inches(11.7)
    section.page_width = Inches(8.3)
    section.left_margin = Inches(1.5)
    section.right_margin = Inches(0.8)
    section.top_margin = Inches(1.2)
    section.bottom_margin = Inches(1.2)
    
    # ===== ТИТУЛЬНЫЙ ЛИСТ =====
    
    # Пустые строки для центрирования
    for _ in range(8):
        doc.add_paragraph()
    
    # Заголовки
    titles = [
        ("МИНОБРНАУКИ РОССИИ", True),
        ("Федеральное государственное бюджетное", False),
        ("образовательное учреждение высшего образования", False),
        ("«ВЛАДИВОСТОКСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»", True),
        ("(ФГБОУ ВО «ВВГУ»)", False),
        ("", False), ("", False),  # Пустые строки
        ("ИНСТИТУТ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И АНАЛИЗА ДАННЫХ", True),
        ("КАФЕДРА ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И СИСТЕМ", True),
    ]
    
    for text, bold in titles:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(14)
        run.font.bold = bold
    
    # Большой отступ
    for _ in range(8):
        doc.add_paragraph()
    
    # Название работы
    work_titles = [
        ("ОТЧЕТ", True, 16),
        ("ПО ЛАБОРАТОРНОЙ РАБОТЕ №1", True, 14),
        ("по дисциплине", False, 14),
        ("«Информатика и программирование»", True, 14),
    ]
    
    for text, bold, size in work_titles:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.font.bold = bold
    
    # Отступ перед данными
    for _ in range(10):
        doc.add_paragraph()
    
    # Данные студента и преподавателя
    student_info = [
        "Студент",
        "гр. BDI-BDZ-21", 
        "Ассистент",
        "преподавателя"
    ]
    
    for text in student_info:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(text)
        run.font.size = Pt(14)
    
    # Отступ для подписей
    for _ in range(4):
        doc.add_paragraph()
    
    # Подписи
    signatures = [
        "_________________________",
        "А.И. Студент",
        "_________________________",
        "М.В. Водяницкий"
    ]
    
    for text in signatures:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(text)
        run.font.size = Pt(14)
    
    # Отступ перед городом
    for _ in range(12):
        doc.add_paragraph()
    
    # Город и год
    p_city = doc.add_paragraph()
    p_city.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_city = p_city.add_run("Владивосток 2025")
    run_city.font.size = Pt(14)
    
    # Разрыв страницы для содержания
    doc.add_page_break()
    
    # ===== СОДЕРЖАНИЕ =====
    
    # Заголовок СОДЕРЖАНИЕ
    p_content = doc.add_paragraph()
    p_content.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_content = p_content.add_run("СОДЕРЖАНИЕ")
    run_content.font.size = Pt(16)
    run_content.font.bold = True
    
    doc.add_paragraph()
    
    # Элементы содержания
    content_items = [
        "1. Введение................................................3",
        "2. Основная часть...........................................4",
        "   2.1. Теоретическая часть................................4",
        "   2.2. Практическая часть..................................5",
        "3. Заключение...............................................6",
        "4. Список использованных источников........................7",
        "5. Приложения...............................................8"
    ]
    
    for item in content_items:
        p = doc.add_paragraph(item)
        p.style = doc.styles['Normal']
    
    # Сохраняем полный документ
    filename = "Полный_отчет_лабораторная_1.docx"
    doc.save(filename)
    
    print(f"Полный отчет создан: {filename}")
    print(f"Путь: {os.path.abspath(filename)}")
    
    return filename

# Установка библиотеки (выполнить в терминале)
def install_requirements():
    """Инструкция по установке необходимых библиотек"""
    print("Для работы программы необходимо установить библиотеку python-docx")
    print("Выполните в командной строке:")
    print("pip install python-docx")
    print("\nИли в терминале VS Code:")
    print("pip install python-docx")

if __name__ == "__main__":
    try:
        # Создаем титульный лист
        create_lab_report_docx()
        
        # Создаем полный отчет
        create_full_lab_report()
        
        print("\n" + "="*50)
        print("Документы успешно созданы!")
        print("Файлы сохранены в текущей папке")
        print("="*50)
        
    except ImportError:
        print("Библиотека python-docx не установлена!")
        install_requirements()