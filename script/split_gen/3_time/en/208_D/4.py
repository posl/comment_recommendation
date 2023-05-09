def floyd_warshall(n, m, a, b, c):
    d = [[float("inf")] * n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[a[i]][b[i]] = c[i]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
