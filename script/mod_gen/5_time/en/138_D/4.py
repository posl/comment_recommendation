def dfs(v, p, x):
    for u in g[v]:
        if u == p:
            continue
        c[u] += x
        dfs(u, v, x)
N, Q = map(int, input().split())
g = [[] for _ in range(N)]
c = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for _ in range(Q):
    p, x = map(int, input().split())
    c[p - 1] += x
dfs(0, -1, 0)
print(*c)

if __name__ == '__main__':
    dfs()