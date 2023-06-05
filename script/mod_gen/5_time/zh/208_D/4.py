def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
n, m = map(int, input().split())
dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
floyd_warshall(n, dist)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][j] == dist[i][k] + dist[k][j]:
                ans += dist[i][j]
print(ans)

if __name__ == '__main__':
    floyd_warshall()