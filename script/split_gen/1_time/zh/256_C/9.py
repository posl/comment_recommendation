def dfs(i,j,grid,h,w):
    if i == 3:
        for k in range(3):
            if grid[0][k] + grid[1][k] + grid[2][k] != w[k]:
                return False
        return True
    if j == 3:
        if grid[i][0] + grid[i][1] + grid[i][2] != h[i]:
            return False
        return dfs(i+1,0,grid,h,w)
    for k in range(1,10):
        grid[i][j] = k
        if dfs(i,j+1,grid,h,w):
            return True
    return False
