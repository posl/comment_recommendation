def floyd_warshall(n, edges):
    # n: number of vertices
    # edges: list of edges, each edge is a tuple (u, v, w)
    # w is the weight of the edge (u, v)
    # return the minimum distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
