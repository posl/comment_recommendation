def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

if __name__ == '__main__':
    floyd_warshall()