def delete():
    N = list(map(int, input("Введіть список = ").split()))
    print("Масив", N)

    result = []
    for x in range(len(N)):
        if x != 1 and x != len(N) - 2:
            result.append(N[x])

    print("Оновлений список", result)
    return result

delete()
