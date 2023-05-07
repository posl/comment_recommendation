def color(graph, node, color):
    if node in graph:
        if color in graph[node]:
            return False
        for n in graph[node]:
            if not color(graph, n, color):
                return False
    return True

if __name__ == '__main__':
    color()