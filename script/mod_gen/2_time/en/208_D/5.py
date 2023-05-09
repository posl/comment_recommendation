def floyd_warshall(n, g):
    d = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i, j, c in g:
        d[i - 1][j - 1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

if __name__ == '__main__':
    floyd_warshall()