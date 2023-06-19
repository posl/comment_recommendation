def dfs(x, y, dist):
    global max_dist
    max_dist = max(max_dist, dist)
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if maze[nx][ny] == '#':
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, dist + 1)
        visited[nx][ny] = False
H, W = map(int, input().split())
maze = [input() for _ in range(H)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
max_dist = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            continue
        visited = [[False]*W for _ in range(H)]
        visited[i][j] = True
        dfs(i, j, 0)
print(max_dist)

if __name__ == '__main__':
    dfs()