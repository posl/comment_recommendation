def dfs(v):
    seen[v] = True
    for i in range(n):
        if graph[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)
n, m = map(int, input().split())
graph = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1
seen = [False for i in range(n)]
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
