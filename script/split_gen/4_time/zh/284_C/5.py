def dfs(x):
    global n, m, g, seen
    seen[x] = True
    for i in range(n):
        if g[x][i] == 1 and seen[i] == False:
            dfs(i)
n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = g[v][u] = 1
seen = [False]*n
ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1
print(ans)
