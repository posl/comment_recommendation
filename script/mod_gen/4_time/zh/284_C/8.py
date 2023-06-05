def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
count = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)

if __name__ == '__main__':
    dfs()