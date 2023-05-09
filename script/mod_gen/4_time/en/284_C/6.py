def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    return visited
N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
count = 0
visited = set()
for vertex in range(1, N+1):
    if vertex not in visited:
        count += 1
        visited = visited | dfs(graph, vertex)
print(count)

if __name__ == '__main__':
    dfs()