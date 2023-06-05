def dfs(i, j, n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(i-1, j-1, n)
    dfs(i-1, j, n)
    dfs(i, j-1, n)
    dfs(i, j+1, n)
    dfs(i+1, j, n)
    dfs(i+1, j+1, n)
