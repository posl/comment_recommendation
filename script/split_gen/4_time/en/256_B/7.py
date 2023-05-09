def problem256_b():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 2
        elif a[i] == 3:
            p += 3
        elif a[i] == 4:
            p += 4
    print(p)
problem256_b()
