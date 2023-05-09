def dfs(v, p):
  for u in g[v]:
    if u == p:
      continue
    c[u] += c[v]
    dfs(u, v)
n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
  a, b = map(int, input().split())
  g[a - 1].append(b - 1)
  g[b - 1].append(a - 1)
c = [0] * n
for i in range(q):
  p, x = map(int, input().split())
  c[p - 1] += x
dfs(0, -1)
print(*c)

if __name__ == '__main__':
    dfs()