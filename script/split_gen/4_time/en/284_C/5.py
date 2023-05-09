def dfs(v, visited, graph):
    visited[v] = True
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph[v][i], visited, graph)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, visited, graph)
        ans += 1
print(ans)
