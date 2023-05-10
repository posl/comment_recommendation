def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 1 << 60
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            p = s[i + 1]
            q = s[j + 1] - s[i + 1]
            r = s[n] - s[j + 1]
            m = max(p, q, r)
            mi = min(p, q, r)
            ans = min(ans, m - mi)
    print(ans)
solve()
