def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001:
        return
    if visited[x][y]:
        return
    if not grid[x][y]:
        return
    visited[x][y] = True
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
grid = [[False] * 2001 for _ in range(2001)]
visited = [[False] * 2001 for _ in range(2001)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    grid[x][y] = True
ans = 0
for i in range(2001):
    for j in range(2001):
        if not visited[i][j] and grid[i][j]:
            dfs(i, j)
            ans += 1
print(ans)
