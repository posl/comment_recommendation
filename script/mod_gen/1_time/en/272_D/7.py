def bfs(graph, start, end, nodes):
    queue = []
    queue.append(start)
    distance = {}
    distance[start] = 0
    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    if end in distance:
        return distance[end]
    else:
        return -1

if __name__ == '__main__':
    bfs()