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
for i in range(m):
    u, v = map(int, input().split())
    if u in graph:
        graph[u].add(v)
    else:
        graph[u] = set([v])
    if v in graph:
        graph[v].add(u)
    else:
        graph[v] = set([u])
for i in range(1, n+1):
    if i not in graph:
        graph[i] = set()
# print(graph)
count = 0
for i in range(1, n+1):
    if i in graph:
        if len(dfs(graph, i)) > 0:
            count += 1
print(count)

if __name__ == '__main__':
    dfs()