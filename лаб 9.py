import csv
import os
flag = False

try:
    csvfile = open("лаб 9(2).csv", "r", encoding="utf-8")
    reader = csv.reader(csvfile)

    print("Вміст файлу:")
    for row in reader:
        print(row)

    csvfile.close()
except FileNotFoundError:
    print("Файл 'лаб 9(2).csv' не знайдено!")
except Exception as e:
    print("Сталася помилка при читанні файлу:", e)

#Пошук найменшого та найбільшого GDP per capita для США (1991–2019)
try:
    csvfile = open("лаб 9(2).csv", "r", encoding="utf-8")
    reader = csv.reader(csvfile)
    usa_data = []
    for row in reader:
        if len(row) >= 7 and row[2] == "United States":
            try:
                year = int(row[4])
                value = float(row[6])
                if 1991 <= year <= 2019:
                    usa_data.append((year, value))
            except:
                pass
    csvfile.close()
    if not usa_data:
        print("Дані для США не знайдено!")
    else:
        #Знаходимо мінімум і максимум
        min_year, min_val = min(usa_data, key=lambda x: x[1])
        max_year, max_val = max(usa_data, key=lambda x: x[1])

        print(f"\nМінімальне значення: {min_val} у {min_year} році")
        print(f"Максимальне значення: {max_val} у {max_year} році")

        #Запис у новий CSV-файл
        with open("результат_лаб9.csv", "w", newline='', encoding="utf-8") as csvfile2:
            writer = csv.writer(csvfile2, delimiter=";")
            writer.writerow(["Тип", "Рік", "Значення"])
            writer.writerow(["Мінімум", min_year, min_val])
            writer.writerow(["Максимум", max_year, max_val])

        print("\nРезультати записано у файл 'результат_лаб9.csv'")

except FileNotFoundError:
    print("Файл 'лаб 9(2).csv' не знайдено!")
except Exception as e:
    print("Сталася помилка при обробці файлу:", e)