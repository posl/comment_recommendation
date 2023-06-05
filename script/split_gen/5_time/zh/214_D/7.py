def get_input():
    n = int(input())
    graph = {}
    for i in range(n-1):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = [(v, w)]
        else:
            graph[u].append((v, w))
        if v not in graph:
            graph[v] = [(u, w)]
        else:
            graph[v].append((u, w))
    return graph
