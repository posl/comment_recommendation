def solve():
    N = int(input())
    if N % 3 == 0:
        print(0)
        return
    if N % 3 == 1:
        if N % 10 == 1:
            print(1)
            return
        if N % 10 == 4:
            print(1)
            return
        if N % 10 == 7:
            print(1)
            return
        if N % 10 == 2:
            print(2)
            return
        if N % 10 == 5:
            print(2)
            return
        if N % 10 == 8:
            print(2)
            return
    if N % 3 == 2:
        if N % 10 == 2:
            print(1)
            return
        if N % 10 == 5:
            print(1)
            return
        if N % 10 == 8:
            print(1)
            return
        if N % 10 == 1:
            print(2)
            return
        if N % 10 == 4:
            print(2)
            return
        if N % 10 == 7:
            print(2)
            return
    print(-1)
solve()
