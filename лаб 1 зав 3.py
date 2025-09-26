N = int(input("Введіть ціле число (1 < N < 9)= "))
while N <= 1 or N >= 9:
    print("Помилка! Число має бути більше 1 і менше 9.")
    exit()
for i in range(1, N + 1):
    for j in range(N, N - i, -1):
        print(j, end=" ")
    print()
