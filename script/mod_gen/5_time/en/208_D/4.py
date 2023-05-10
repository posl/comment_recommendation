def floyd_warshall(n, edges):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for a, b, c in edges:
        dist[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

if __name__ == '__main__':
    floyd_warshall()