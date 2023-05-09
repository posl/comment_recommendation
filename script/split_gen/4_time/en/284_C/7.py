def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)
n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = True
visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)
