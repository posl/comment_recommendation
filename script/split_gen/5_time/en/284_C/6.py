def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited
n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
ans = 0
for i in range(1, n+1):
    if i not in graph[i]:
        ans += 1
        dfs(graph, i)
print(ans)
