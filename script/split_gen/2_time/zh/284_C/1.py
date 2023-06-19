def dfs(x):
    visited[x] = True
    for i in range(1, N+1):
        if graph[x][i] == 1 and not visited[i]:
            dfs(i)
N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)
