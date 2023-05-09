def dfs(v, p, d, c):
    c[v] += d
    for i in g[v]:
        if i == p:
            continue
        dfs(i, v, d, c)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
c = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    dfs(p, -1, x, c)
print(*c)
