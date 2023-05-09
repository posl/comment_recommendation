def dfs(v, p):
  #print(v, p)
  c = 1
  for u in G[v]:
    if u == p:
      continue
    if c == color[v]:
      c += 1
    color[u] = c
    c += 1
    dfs(u, v)
N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
color = [-1] * N
color[0] = 1
dfs(0, -1)
print(max(color))
for i in range(N-1):
  print(color[i+1])
