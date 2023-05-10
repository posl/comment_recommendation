def dfs(v, p, d):
    for nv in g[v]:
        if nv == p:
            continue
        depth[nv] = d + 1
        dfs(nv, v, d + 1)
N, Q = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
depth = [0] * N
dfs(0, -1, 0)
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    print(depth[p] + x)
