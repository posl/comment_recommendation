def dfs(v, p, x):
    for nv in G[v]:
        if nv == p: continue
        cnt[nv] += x
        dfs(nv, v, x)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
cnt = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0, -1, 0)
print(*cnt)
