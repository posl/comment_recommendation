def dfs(grid, x, y):
    if grid[x][y] == 1:
        return
    grid[x][y] = 1
    if x > 0:
        dfs(grid, x-1, y)
    if y > 0:
        dfs(grid, x, y-1)
    if x < 1:
        dfs(grid, x+1, y)
    if y < 1:
        dfs(grid, x, y+1)
