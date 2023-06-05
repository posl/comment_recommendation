def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += a[i] / b[i]
    ans /= 2
    for i in range(n):
        ans -= a[i] / b[i]
        if ans < 0:
            ans += a[i] / b[i]
            break
    print(ans)
solve()
