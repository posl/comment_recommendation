def dijkstra(s, n, d):
    INF = 10 ** 9
    dist = [INF] * n
    dist[s] = 0
    used = [False] * n
    while True:
        v = -1
        for u in range(n):
            if (not used[u]) and (v == -1):
                v = u
            elif (not used[u]) and dist[u] < dist[v]:
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(n):
            dist[u] = min(dist[u], dist[v] + d[v][u])
    return dist
n, m = map(int, input().split())
d = [[10 ** 9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    for i in range(n):
        for j in range(n):
            if d[i][j] < 10 ** 9:
                ans += d[i][j]
print(ans)
