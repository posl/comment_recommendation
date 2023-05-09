def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest paths.
    graph is a dictionary, where each key is a vertex and each value is a list of
    (vertex, distance) tuples. start is the starting vertex.
    """
    Q = set(graph)  # remaining vertices
    dist = dict.fromkeys(graph, float('inf'))  # distance from start
    dist[start] = 0
    while Q:
        u = min(Q, key=dist.get)  # vertex with smallest distance
        Q.remove(u)
        for v, d in graph[u].items():  # all neighbors of u
            if v in Q:
                dist[v] = min(dist[v], dist[u] + d)  # relax (u,v,d)
    return dist

if __name__ == '__main__':
    dijkstra()