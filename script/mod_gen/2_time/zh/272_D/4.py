def bfs(sx, sy):
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    que = []
    que.append((sx, sy))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny]==-1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    return dist
N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dist = bfs(0, 0)
for i in range(N):
    for j in range(N):
        if dist[i][j] == -1 or dist[i][j] > M:
            print(-1, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

if __name__ == '__main__':
    bfs()