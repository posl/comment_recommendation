def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return len(path)-1
        if node in visited:
            continue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
        visited.add(node)
    return -1

if __name__ == '__main__':
    bfs()