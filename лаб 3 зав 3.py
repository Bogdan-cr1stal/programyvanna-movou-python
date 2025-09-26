sentence = str(input("Введіть речення - "))
while len(sentence.strip()) == 0:
    sentence = str(input("Речення порожнє, введіть ще раз - "))

words = sentence.split()
result = []

for i in words:
    if len(i) > 1 and i[0].lower() == i[-1].lower():
        result.append(i)

if result:
    print("Слова, які починаються і закінчуються на одну й ту ж літеру:", ", ".join(result))
else:
    print("У реченні немає слів які починаються і закінчуються на одну й туж літеру")
