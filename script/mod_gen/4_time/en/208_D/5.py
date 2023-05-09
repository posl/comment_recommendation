def floyd_warshall(n, edges):
    INF = 10**18
    d = [[INF]*n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b, c in edges:
        d[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

if __name__ == '__main__':
    floyd_warshall()