def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            return path
        else:
            for m in graph[n]:
                if m not in path:
                    queue.append((m, path+[m]))
