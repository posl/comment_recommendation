def dfs(v):
    seen[v] = True
    for next_v in range(n):
        if graph[v][next_v] == 0:
            continue
        if seen[next_v]:
            continue
        dfs(next_v)
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = graph[v][u] = 1
seen = [False] * n
ans = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)
