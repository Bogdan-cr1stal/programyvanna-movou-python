N = 7
matrix = [[(j - i + 1) * (j >= i) for j in range(N)] for i in range(N)]

for k in matrix:
        print(*k)