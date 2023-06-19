def floyd_warshall(N, M, A, B, C):
    dist = [[float('inf') for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(M):
        dist[A[i]-1][B[i]-1] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

if __name__ == '__main__':
    floyd_warshall()