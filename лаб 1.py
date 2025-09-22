
a = float(input("Введіть a = "))
b = float(input("Введіть b = "))

if a < 0 or b < 0:
    print("Помилка: числа a та b повинні бути додатними.")
    exit()

if a > b:
    X = a / b - 1
elif a == b:
    X = -25
else:
    X = (a**3 - 5) / a

print("Результат: X =", X)
