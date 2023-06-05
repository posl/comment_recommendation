def solve():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 0)
    elif L == 3:
        print(3, 2)
        print(1, 2, 0)
        print(2, 3, 1)
    elif L == 4:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 2)
        print(2, 4, 0)
    elif L == 5:
        print(5, 7)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    else:
        print(L, L - 1)
        for i in range(1, L):
            print(i, i + 1, 0)
solve()
