N = int(input("Введіть довжину масиву N= "))
while N <= 0:
    N = int(input("Довжина має бути більше 0. Введіть ще раз: "))

arr = [int(input()) for _ in range(N)]
min = min(arr)

print("Масив:", arr)

print("Мінімальний елемент масиву:", min)
