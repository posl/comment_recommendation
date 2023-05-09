def dfs(v, p, d):
  for u in G[v]:
    if u == p: continue
    d[u] += d[v]
    dfs(u, v, d)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
d = [0] * N
for _ in range(Q):
  p, x = map(int, input().split())
  d[p-1] += x
dfs(0, -1, d)
print(*d)
