def dfs(v, p, d):
    global depth
    depth[v] = d
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
depth = [0] * n
dfs(0, -1, 0)
cnt = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p - 1] += x
for i in range(n):
    print(cnt[i] + depth[i], end=" ")
