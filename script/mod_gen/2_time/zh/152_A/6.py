def bfs(sx, sy):
    dist = [[-1] * w for _ in range(h)]
    dist[sx][sy] = 0
    que = []
    que.append((sx, sy))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != '#' and dist[nx][ny] == -1:
                que.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    res = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '#' and dist[i][j] != -1:
                res = max(res, dist[i][j])
    return res
h, w = map(int, input().split())
maze = [input() for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
for sx in range(h):
    for sy in range(w):
        if maze[sx][sy] == '#':
            continue
        ans = max(ans, bfs(sx, sy))
print(ans)

if __name__ == '__main__':
    bfs()