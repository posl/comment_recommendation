def bfs(start, end, graph):
    visited = [0] * (len(graph) + 1)
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
    return False

if __name__ == '__main__':
    bfs()