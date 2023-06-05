def f(a):
    if a % 2 == 0:
        return a // 2
    if a % 3 == 0:
        return a // 3
    return -1
n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    for i in range(n):
        if a[i] % 2 == 1:
            print(ans)
            exit()
        a[i] = f(a[i])
    ans += 1
