def check_grid(grid):
    for i in range(0, len(grid) - 5):
        for j in range(0, len(grid) - 5):
            if grid[i][j] == '#' and grid[i + 1][j + 1] == '#' and grid[i + 2][j + 2] == '#' and grid[i + 3][j + 3] == '#' and grid[i + 4][j + 4] == '#' and grid[i + 5][j + 5] == '#':
                return True
            if grid[i + 5][j] == '#' and grid[i + 4][j + 1] == '#' and grid[i + 3][j + 2] == '#' and grid[i + 2][j + 3] == '#' and grid[i + 1][j + 4] == '#' and grid[i][j + 5] == '#':
                return True
    return False

if __name__ == '__main__':
    check_grid()