def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
n, m = map(int, input().split())
d = [[float('inf')]*n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
floyd_warshall()
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                ans += d[i][j] + d[j][k] + d[k][i]
print(ans)

if __name__ == '__main__':
    floyd_warshall()