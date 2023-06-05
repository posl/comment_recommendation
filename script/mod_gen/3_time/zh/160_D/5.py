def floyd(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    dist[j][i] = dist[i][j]
    return dist

if __name__ == '__main__':
    floyd()