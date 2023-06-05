def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    p = list(range(n))
    def root(x):
        if p[x] != x: p[x] = root(p[x])
        return p[x]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    for i in range(m):
        p[root(a[i][0])] = root(a[i][1])
    q = list(range(n))
    for i in range(m):
        q[root(c[i][0])] = root(c[i][1])
    print("Yes" if p == q else "No")
solve()
