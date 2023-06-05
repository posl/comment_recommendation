def dfs(v):
    seen[v] = True
    for i in range(1,n+1):
        if not seen[i] and g[v][i] == 1:
            dfs(i)
n,m = map(int,input().split())
g = [[0 for i in range(n+1)] for j in range(n+1)]
seen = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a][b] = g[b][a] = 1
ans = 0
for i in range(1,n+1):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)
