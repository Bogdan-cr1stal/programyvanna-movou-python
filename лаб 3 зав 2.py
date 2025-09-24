word_1 = str(input("Введіть перше слово: "))
word_2 = str(input("Введіть друге слово: "))

while (len(word_1) == 0 or word_1.isdigit()) or (len(word_2) == 0 or word_2.isdigit()):
    print("Помилка! Введено некоректні слова.")
    word_1 = str(input("Введіть перше слово ще раз: "))
    word_2 = str(input("Введіть друге слово ще раз: "))

result = ""

for ch in word_1:
    if ch not in word_2:
        result += ch

for ch in word_2:
    if ch not in word_1:
        result += ch

print("Літери, які є тільки в одному з двох слів:", result)