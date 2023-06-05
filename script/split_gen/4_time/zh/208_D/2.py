def floyd_warshall(n, m, edges):
    d = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b, c in edges:
        d[a - 1][b - 1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
