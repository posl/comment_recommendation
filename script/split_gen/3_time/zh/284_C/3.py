def dfs(v):
    global n, m, g, seen
    seen[v] = True
    for i in range(n):
        if g[v][i] == 1 and seen[i] == False:
            dfs(i)
n, m = map(int, input().split())
g = [[0]*n for i in range(n)]
seen = [False]*n
for i in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = 1
    g[b-1][a-1] = 1
ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1
print(ans)
