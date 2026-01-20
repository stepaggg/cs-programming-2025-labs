# Задание 1
objects = [("Containment Cell A", 4), ("Archive Vault", 1), ("Bio Lab Sector", 3), ("Observation Wing", 2)]
print("1. Сортировка по уровню угрозы:")
print(sorted(objects, key=lambda x: x[1]))

# Задание 2
staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
total_costs = list(map(lambda emp: emp["shift_cost"] * emp["shifts"], staff_shifts))
print("\n2. Общая стоимость работы:")
print(total_costs)
print("Максимальная стоимость:", max(total_costs))

# Задание 3
personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
personnel_cat = list(map(lambda p: {
    "name": p["name"], 
    "clearance": p["clearance"],
    "category": "Restricted" if p["clearance"] == 1 
                else "Confidential" if p["clearance"] in [2, 3] 
                else "Top Secret"
}, personnel))
print("\n3. Категории допуска:")
print(personnel_cat)

# Задание 4
zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
day_zones = list(filter(lambda z: z["active_from"] >= 8 and z["active_to"] <= 18, zones))
print("\n4. Дневные зоны:")
print(day_zones)

# Задание 5
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"}
]
links_reports = list(filter(lambda r: "http://" in r["text"] or "https://" in r["text"], reports))
import re
cleaned_reports = list(map(lambda r: {"author": r["author"], "text": re.sub(r'https?://[^\s]+', '[ДАННЫЕ УДАЛЕНЫ]', r["text"])}, links_reports))
print("\n5. Отчеты без ссылок:")
print(cleaned_reports)

# Задание 6
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
enhanced = list(filter(lambda scp: scp["class"] != "Safe", scp_objects))
print("\n6. Усиленные меры содержания:")
print(enhanced)

# Задание 7
incidents = [{"id": 101, "staff": 4}, {"id": 102, "staff": 12}, {"id": 103, "staff": 7}, {"id": 104, "staff": 20}]
top_three = sorted(incidents, key=lambda x: x["staff"], reverse=True)[:3]
print("\n7. Топ-3 инцидента:")
print(top_three)

# Задание 8
protocols = [("Lockdown", 5), ("Evacuation", 4), ("Data Wipe", 3), ("Routine Scan", 1)]
protocol_strings = list(map(lambda p: f"Protocol {p[0]} - Criticality {p[1]}", protocols))
print("\n8. Протоколы:")
print(protocol_strings)

# Задание 9
shifts = [6, 12, 8, 24, 10, 4]
normal_shifts = list(filter(lambda s: 8 <= s <= 12, shifts))
print("\n9. Нормальные смены:")
print(normal_shifts)

# Задание 10
evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
best = max(evaluations, key=lambda e: e["score"])
print("\n10. Лучший сотрудник:")
print(f"{best['name']} - {best['score']} баллов")