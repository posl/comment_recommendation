def dfs(v,p):
  ans.append(v)
  for i in range(len(g[v])):
    if g[v][i] != p:
      dfs(g[v][i],v)
      ans.append(v)
n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  g[a].append(b)
  g[b].append(a)
for i in range(n):
  g[i].sort()
ans = []
dfs(0,-1)
print(*[i+1 for i in ans])

if __name__ == '__main__':
    dfs()