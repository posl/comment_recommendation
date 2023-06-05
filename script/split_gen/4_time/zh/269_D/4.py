def dfs(i, j, visited, grid, n):
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1 and not visited[ni][nj]:
            dfs(ni, nj, visited, grid, n)
n = int(input())
grid = [[0 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
for _ in range(n):
    x, y = map(int, input().split())
    grid[x + n - 1][y + n - 1] = 1
di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
visited = [[False for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
ans = 0
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j, visited, grid, 2 * n - 1)
            ans += 1
print(ans)
