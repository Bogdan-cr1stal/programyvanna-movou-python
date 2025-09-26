def search():
    A = input("Введіть текст - ")
    B = A.lower()

    print("Текст - ", B)

    counts = {}
    for i in B:
        if i.isalpha():
            counts[i] = counts.get(i, 0) + 1

    many = set([i for i, cnt in counts.items() if cnt >= 2])
    once = set([i for i, cnt in counts.items() if cnt == 1])

    print("Літери, які входять не менше двох разів", many if many else set(list(many)))
    print("Літери, які входять по одному разу", once if once else set(list(once)))

search()
