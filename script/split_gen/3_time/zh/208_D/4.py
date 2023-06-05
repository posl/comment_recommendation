def floyd_warshall(N, M, edges):
    # dist[i][j]: 从i到j的最短路径长度
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for (a, b, c) in edges:
        dist[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
