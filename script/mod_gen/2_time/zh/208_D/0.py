def floyd_warshall(n, m, edges):
    dist = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for a, b, c in edges:
        dist[a][b] = c
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == '__main__':
    floyd_warshall()