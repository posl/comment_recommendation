def solve():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N,a)
    #print(len(a))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        exit()
    if N == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        elif a[0] == 2 and a[1] == 1:
            print(1)
        else:
            print(-1)
        exit()
    if N == 3:
        if a[0] == 1 and a[1] == 3 and a[2] == 2:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3:
            print(1)
        else:
            print(-1)
        exit()
    if N == 4:
        if a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 4 and a[3] == 2:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 3 and a[3] == 2:
            print(2)
        else:
            print(-1)
        exit()
    if N == 5:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 5 and a[4] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 5 and a[4] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 2
