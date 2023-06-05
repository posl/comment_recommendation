def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
                res += 1
                flag = False
                break
        if flag:
            break
    while True:
        flag = True
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] = a[i] / 3
                res += 1
                flag = False
                break
        if flag:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(res)
