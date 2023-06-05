def floyd_warshall(n, d):
    # n: the number of vertices
    # d: distance matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
n, m = map(int, input().split())
d = [[10**9] * n for i in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
floyd_warshall(n, d)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[i][j] == d[i][k] + d[k][j]:
                ans += d[i][j]
print(ans)
