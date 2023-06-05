def dfs(v):
    seen[v] = True
    for i in range(n):
        if not g[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)
n,m = map(int,input().split())
g = [[False]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = g[b-1][a-1] = True
seen = [False]*n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
