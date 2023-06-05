def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        y = a[n - 1 - i]
        if x > y:
            x, y = y, x
        if x == 0 and y == 0:
            ans += 2
        elif x == 0:
            ans += 1
        elif x == y:
            ans += 1
        else:
            ans += 2
    print(ans // 2)
