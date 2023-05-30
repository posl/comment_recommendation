def func(n, a):
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                break
        else:
            cnt += 1
            continue
        break
    if a.count(a[0]) == n:
        return cnt
    else:
        return -1
n = int(input())
a = list(map(int, input().split()))
print(func(n, a))
