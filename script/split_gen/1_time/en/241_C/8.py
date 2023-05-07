def check_grid(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ".":
                grid[i][j] = 0
            else:
                grid[i][j] = 1
    return grid
