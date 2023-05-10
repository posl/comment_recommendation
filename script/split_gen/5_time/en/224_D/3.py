def bfs(graph, start):
    visited = [False] * 9
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited
