def add_to_grid(grid, x, y):
    if x not in grid:
        grid[x] = {}
    grid[x][y] = True
