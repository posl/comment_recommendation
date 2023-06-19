def dfs(v, p):
    global ans
    ans.append(v)
    for u in g[v]:
        if u != p:
            dfs(u, v)
            ans.append(v)
n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
ans = []
dfs(x, -1)
print(*ans)
