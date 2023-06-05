def solve():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 1)
    elif w <= 5:
        print(2)
        print(2, 3)
    else:
        print(6)
        print(1, 2, 4, 5, 7, 8)
solve()
