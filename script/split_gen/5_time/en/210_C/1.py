def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = d.get(c[i], 0) + 1
    ans = len(d)
    for i in range(n - k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        d[c[i + k]] = d.get(c[i + k], 0) + 1
        ans = max(ans, len(d))
    print(ans)
