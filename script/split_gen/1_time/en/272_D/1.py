def bfs(sx, sy):
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    que = deque([(sx, sy)])
    while que:
        x, y = que.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    return dist
N, M = map(int, input().split())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = bfs(0, 0)
for i in range(N):
    for j in range(N):
        if dist[i][j] == -1:
            print(-1, end=" ")
        else:
            print(dist[i][j] // 2 + 1, end=" ")
    print()
