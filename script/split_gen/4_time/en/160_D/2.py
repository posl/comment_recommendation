def floyd_warshall(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
n, x, y = map(int, input().split())
x -= 1
y -= 1
d = [[n] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(n - 1):
    d[i][i + 1] = 1
    d[i + 1][i] = 1
d[x][y] = 1
d[y][x] = 1
d = floyd_warshall(d, n)
ans = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        ans[d[i][j]] += 1
print(*ans[1:], sep='\n')
