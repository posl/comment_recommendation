def bfs(start, goal, graph):
    queue = [(start, 0)]
    done = set()
    while queue:
        node, depth = queue.pop(0)
        if node == goal:
            return depth
        if node in done:
            continue
        done.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, depth + 1))
    return None
