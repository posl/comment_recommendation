def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(n):
        ans += a[i] ** 2 * (n - 1)
        ans -= 2 * a[i] * (s[n] - s[i + 1])
    print(ans)
