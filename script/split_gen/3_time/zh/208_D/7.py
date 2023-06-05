def floyd_warshall(n, m, roads):
    inf = 10 ** 9
    dist = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for road in roads:
        dist[road[0]][road[1]] = road[2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for i in range(m)]
dist = floyd_warshall(n, m, roads)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][j] == dist[i][k] + dist[k][j]:
                ans += dist[i][j]
print(ans)
