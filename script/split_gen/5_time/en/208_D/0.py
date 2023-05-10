def floyd_warshall(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
n, m = map(int, input().split())
d = [[float("inf") for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
d = floyd_warshall(d)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[i][j] == d[i][k] + d[k][j]:
                ans += d[i][j]
print(ans)
