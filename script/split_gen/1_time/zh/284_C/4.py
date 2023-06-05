def dfs(v):
    seen[v] = True
    for i in range(n):
        if not G[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)
n,m = map(int,input().split())
G = [[False]*n for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u][v] = G[v][u] = True
seen = [False]*n
res = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    res += 1
print(res)
