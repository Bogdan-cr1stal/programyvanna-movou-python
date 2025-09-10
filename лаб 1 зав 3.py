N = int(input("Введіть ціле число (1 < N < 9)= "))

for i in range(1, N + 1):
    for j in range(N, N - i, -1):
        print(j, end=" ")
    print()
