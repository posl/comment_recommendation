def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 0 or seen[i]:
            continue
        dfs(i)
n,m = map(int,input().split())
G = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a-1][b-1] = G[b-1][a-1] = 1
seen = [False]*n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
