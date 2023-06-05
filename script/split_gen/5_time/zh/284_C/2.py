def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
n, m = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1] = set()
for i in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
count = 0
visited = set()
for i in range(1, n+1):
    if i not in visited:
        visited.update(dfs(graph, i))
        count += 1
print(count)
