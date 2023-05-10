def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        depth[u] = depth[v] + 1
        dfs(u, v)
n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
depth = [0] * n
dfs(x, -1)
print(depth[y])
