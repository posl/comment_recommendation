def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for a, b, c in edges:
        dist[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    edges[i][0] -= 1
    edges[i][1] -= 1
dist = floyd_warshall(n, edges)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][k] + dist[k][j] == dist[i][j]:
                ans += dist[i][j]
print(ans)

if __name__ == '__main__':
    floyd_warshall()