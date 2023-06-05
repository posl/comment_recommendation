def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    m1 = [0] * (n + 1)
    m2 = [0] * (n + 1)
    m3 = [0] * (n + 1)
    for i in range(1, n + 1):
        m1[i] = max(m1[i - 1], s[i] - p)
        m2[i] = max(m2[i - 1], s[i] - q)
        m3[i] = max(m3[i - 1], s[i] - r)
    ans = 0
    for i in range(n + 1):
        ans = max(ans, m1[i] + m2[i] + m3[i])
    print(ans)
solve()
