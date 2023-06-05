def solve():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        l[a] += 1
        r[b] += 1
    ans = 0
    now = 0
    for i in range(1, n + 1):
        now += l[i]
        if now == m:
            ans += 1
        now -= r[i]
    print(ans)
