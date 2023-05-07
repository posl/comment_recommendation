def dfs(v, p, d):
    dist[v] = d
    for nv in g[v]:
        if nv == p: continue
        dfs(nv, v, d + 1)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
dist = [0] * n
dfs(0, -1, 0)
for _ in range(q):
    p, x = map(int, input().split())
    p = p - 1
    print(dist[p] + x)

if __name__ == '__main__':
    dfs()