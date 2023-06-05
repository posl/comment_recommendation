def solve():
    n, w = map(int, input().split())
    d = {}
    for _ in range(n):
        s, t, p = map(int, input().split())
        if s not in d:
            d[s] = 0
        d[s] += p
        if t not in d:
            d[t] = 0
        d[t] -= p
    for k in sorted(d.keys()):
        w -= d[k]
        if w < 0:
            print("No")
            return
    print("Yes")
solve()
