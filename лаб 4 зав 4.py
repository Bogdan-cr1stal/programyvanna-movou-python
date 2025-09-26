def find_5():
    N = list(map(int, input("Введіть елементи списку = ").split()))
    print("Початковий список:", N)

    if len(N) < 5:
        print("У списку менше ніж 5 елементів!")
        return N

    sorted_list = sorted(N, reverse=True)

    find_5 = sorted_list[:5]

    print("Перші п’ять максимальних елементів:", find_5)
    return find_5
find_5()
