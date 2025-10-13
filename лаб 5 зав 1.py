#Словник
#Ключ — номер телефону, значення — прізвище

phones = {
    "380681234567": "Мельник",
    "380698901111": "Шевченко",
    "380961112233": "Коваленко",
    "380974445566": "Бондаренко",
    "380987778899": "Бойко",
    "380990007777": "Ткаченко",
    "380662224455": "Кравченко",
    "380681234000": "Ковальчук",
    "380983456789": "Коваль",
    "380963333222": "Олійник"
}

#Функції

def Print(phone):#Вивід словника на екран
    print("Вміст записника ")
    for key in phone:
        print("Номер - ", key, " Прізвище - ", phone[key])
    print()

def add(phone, key, surname):#Додавання даних у словник
    phone[key] = surname
    print("Додано запис - ", key, "-", surname,"\n")

def Del(phone, key):#Видалення даних зі словника
    if key in phone:
        del phone[key]
        print("Видалено запис із номером - ", key, "\n")
    else:
        print("Такого номера немає у словнику.\n")

def print_sort(phone):#Сортування словника за ключем
    sorted_book = {k: phone[k] for k in sorted(phone)}
    print("Відсортований записник - ")
    for key in sorted_book:
        print("Номер - ", key, " - Прізвище - ", sorted_book[key])
    print()

def find_by_name(phone):#Пошук номера за прізвищем
    surname = input("Введіть прізвище - ")
    found = False
    for key in phone:
        if phone[key].lower() == surname.lower():
            print("Номер телефону для", surname, "-", key)
            found = True
    if not found:
        print("Такої особи немає у записнику.\n")
    print()


def find_by_phone(phone):#Пошук прізвища за номером
    key = input("Введіть номер телефону - ")
    if key in phone:
        print("Номер", key, "належить - ", phone[key])
    else:
        print("Такого номера немає у записнику\n")
    print()

def main():
    while True:
        print("Виберіть бажану дію")
        print("1 — Вивести всі записи")
        print("2 — Додати запис")
        print("3 — Видалити запис")
        print("4 — Відсортувати за номерами")
        print("5 — Знайти номер за прізвищем")
        print("6 — Знайти прізвище за номером")
        print("0 — Вихід")

        choice = input("Ваш вибір - ")

        if choice == "1":
            Print(phones)
        elif choice == "2":
            key = input("Введіть номер телефону - ")
            surname = input("Введіть прізвище - ")
            add(phones, key, surname)
        elif choice == "3":
            key = input("Введіть номер для видалення - ")
            Del(phones, key)
        elif choice == "4":
            print_sort(phones)
        elif choice == "5":
            find_by_name(phones)
        elif choice == "6":
            find_by_phone(phones)
        elif choice == "0":
            print("Роботу завершено")
            break
        else:
            print("Невірний вибір!\n")
main()