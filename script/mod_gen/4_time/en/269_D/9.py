def add_to_grid(grid, x, y):
    if x not in grid:
        grid[x] = {}
    grid[x][y] = True

if __name__ == '__main__':
    add_to_grid()