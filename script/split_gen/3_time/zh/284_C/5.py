def dfs(now, last):
    if last != -1:
        visited[now] = True
    for i in range(n):
        if not visited[i] and graph[now][i]:
            dfs(i, now)
n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = graph[v - 1][u - 1] = True
visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i, -1)
        count += 1
print(count)
