def check_6x6(grid):
    # check horizontal
    for i in range(0, len(grid)):
        for j in range(0, len(grid) - 5):
            if grid[i][j] == '#' and grid[i][j + 1] == '#' and grid[i][j + 2] == '#' and grid[i][j + 3] == '#' and \
                    grid[i][j + 4] == '#' and grid[i][j + 5] == '#':
                return True
    # check vertical
    for i in range(0, len(grid) - 5):
        for j in range(0, len(grid)):
            if grid[i][j] == '#' and grid[i + 1][j] == '#' and grid[i + 2][j] == '#' and grid[i + 3][j] == '#' and \
                    grid[i + 4][j] == '#' and grid[i + 5][j] == '#':
                return True
    # check diagonal
    for i in range(0, len(grid) - 5):
        for j in range(0, len(grid) - 5):
            if grid[i][j] == '#' and grid[i + 1][j + 1] == '#' and grid[i + 2][j + 2] == '#' and grid[i + 3][
                j + 3] == '#' and grid[i + 4][j + 4] == '#' and grid[i + 5][j + 5] == '#':
                return True
    return False
