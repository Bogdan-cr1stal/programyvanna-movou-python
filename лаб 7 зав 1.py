def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "не було відкрито!")
        return None
    else:
        print("File", file_name, "Файл відкрито")
        return file

file1_name = "TF8_1.txt"
file2_name = "TF8_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    file_1_w.write("Кун-фу Панда123\n")
    file_1_w.write("Як приборкати дракона456\n")
    file_1_w.write("Звірополіс789\n")
    print("Інформацію успішно додано до TF8_1.txt!")
    file_1_w.close()
    print("Файл TF8_1.txt було закрито!\n")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    data = file_2_r.read()

    #Видаляємо цифри і символи нового рядка
    filtered = ''.join(ch for ch in data if not ch.isdigit())
    filtered = filtered.replace('\n', ' ') #замінюємо переведення рядків на пробіли

    #Розбиваємо на частини по 10 символів
    parts = [filtered[i:i + 10] for i in range(0, len(filtered), 10)]

    #Записуємо у TF8_2 з номерами
    for i, part in enumerate(parts, start=1):
        file_2_w.write(f"{i:5d} {part}\n")

    print("Інформацію успішно додано до TF8_2.txt!")
    file_2_r.close()
    file_2_w.close()
    print("Файли TF8_1.txt та TF8_2.txt були закриті!\n")


#Читання TF8_2 та виведення
print("Вміст TF8_2")
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())
    print("Файл TF8_2.txt було закрито!")
    file_3_r.close()
