def dfs(u):
    global visited
    visited[u] = True
    for v in range(n):
        if not visited[v] and G[u][v]:
            dfs(v)
n, m = map(int, input().split())
G = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = True
visited = [False] * n
ans = 0
for u in range(n):
    if not visited[u]:
        dfs(u)
        ans += 1
print(ans)
