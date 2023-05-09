def solve(l):
    if l == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    if l == 3:
        print(3, 2)
        print(1, 2, 0)
        print(2, 3, 1)
        return
    if l == 4:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        return
    if l == 5:
        print(5, 7)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
        return
    print(l + 1, l + l - 1)
    for i in range(1, l):
        print(i, i + 1, 0)
    print(1, l + 1, 1)
    for i in range(1, l):
        print(i, i + 1, 1)
