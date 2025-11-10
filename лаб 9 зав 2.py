import json
import os

DATA_FILE = "phonebook.json"
RESULT_FILE = "result.json"

#Початкові дані
initial_phonebook = [
    {"Surname": "Мельник", "Phone": "380681234567"},
    {"Surname": "Шевченко", "Phone": "380698901111"},
    {"Surname": "Коваленко", "Phone": "380961112233"},
    {"Surname": "Бондаренко", "Phone": "380974445566"},
    {"Surname": "Бойко", "Phone": "380987778899"},
    {"Surname": "Ткаченко", "Phone": "380990007777"},
    {"Surname": "Кравченко", "Phone": "380662224455"},
    {"Surname": "Ковальчук", "Phone": "380681234000"},
    {"Surname": "Коваль", "Phone": "380983456789"},
    {"Surname": "Олійник", "Phone": "380963333222"}
]

#Створення файлу при першому запуску
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(initial_phonebook, file, ensure_ascii=False, indent=4)

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

#функція — додає результат до result.json без очищення
def save_result(new_result):
    if os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, "r", encoding="utf-8") as file:
            try:
                results = json.load(file)
            except json.JSONDecodeError:
                results = []
    else:
        results = []
    results.append(new_result)
    with open(RESULT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

def show_data():
    data = load_data()
    print("\nВміст телефонного записника:")
    for p in data:
        print(f"{p['Surname']}: {p['Phone']}")
    print()

def add_entry():
    data = load_data()
    surname = input("Введіть прізвище: ")
    phone = input("Введіть номер телефону: ")
    data.append({"Surname": surname, "Phone": phone})
    save_data(data)
    print("Запис додано!\n")

def delete_entry():
    data = load_data()
    surname = input("Введіть прізвище для видалення: ")
    new_data = [p for p in data if p["Surname"].lower() != surname.lower()]
    if len(new_data) == len(data):
        print("Такого прізвища не знайдено.")
    else:
        save_data(new_data)
        print("Запис видалено!\n")

def search_entry():
    data = load_data()
    print("\n1 - Пошук за прізвищем")
    print("2 - Пошук за номером")
    choice = input("Ваш вибір: ")

    if choice == "1":
        surname = input("Введіть прізвище: ")
        result = [p for p in data if p["Surname"].lower() == surname.lower()]
    elif choice == "2":
        phone = input("Введіть номер телефону: ")
        result = [p for p in data if p["Phone"] == phone]
    else:
        print("Невірний вибір.")
        return

    if result:
        print("Знайдено:")
        for p in result:
            print(f"{p['Surname']}: {p['Phone']}")
    else:
        print("Нічого не знайдено.")

    save_result({"Тип": "Пошук", "Результат": result})
    print(f"Результат додано у файл {RESULT_FILE}\n")

def task_a():
    data = load_data()
    surname = input("Введіть прізвище особи: ")
    result = [p for p in data if p["Surname"].lower() == surname.lower()]
    if result:
        print(f"Телефон {surname}: {result[0]['Phone']}")
    else:
        print("Такої особи не знайдено.")
    save_result({"Тип": "Телефон за прізвищем", "Результат": result})
    print(f"Результат додано у файл {RESULT_FILE}\n")

def task_b():
    data = load_data()
    phone = input("Введіть номер телефону: ")
    result = [p for p in data if p["Phone"] == phone]
    if result:
        print(f"Номер {phone} належить: {result[0]['Surname']}")
    else:
        print("Такого номера немає.")
    save_result({"Тип": "Прізвище за номером", "Результат": result})
    print(f"Результат додано у файл {RESULT_FILE}\n")

#Головне меню
while True:
    print("=== ТЕЛЕФОННИЙ ЗАПИСНИК ===")
    print("1 - Вивести всі дані")
    print("2 - Додати запис")
    print("3 - Видалити запис")
    print("4 - Пошук за полем")
    print("5 - Телефон певної особи")
    print("6 - Прізвище за номером")
    print("7 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_data()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        delete_entry()
    elif choice == "4":
        search_entry()
    elif choice == "5":
        task_a()
    elif choice == "6":
        task_b()
    elif choice == "7":
        print("Вихід із програми.")
        break
    else:
        print("Невірний вибір!\n")