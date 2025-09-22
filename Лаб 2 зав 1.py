import math

def function(alpha):
    z = (math.sqrt(2) / 2) * math.sin(alpha / 2)
    return z

def amebas(n):
    num = n // 3
    return 2 ** num

alpha = float(input("Введіть значення α = "))
print("Значення виразу z = ", function(alpha))

n = int(input("Введіть кількість годин n = "))
print("Через", n, "годин буде", amebas(n), "амеб")