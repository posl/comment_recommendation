def floyd_warshall(n, m, edges):
    inf = float("inf")
    dist = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for edge in edges:
        a, b, c = edge
        dist[a-1][b-1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist
