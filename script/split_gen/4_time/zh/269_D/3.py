def dfs(x, y):
    global dx, dy, N, grid
    grid[x][y] = 0
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
            dfs(nx, ny)
N = int(input())
grid = [[0] * 2000 for _ in range(2000)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
for i in range(N):
    x, y = map(int, input().split())
    x += 500
    y += 500
    grid[x][y] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)
