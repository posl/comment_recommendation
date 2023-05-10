def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
    return visited
