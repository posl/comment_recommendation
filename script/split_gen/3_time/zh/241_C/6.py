def is_ok(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '#':
                if i+5 < len(grid) and grid[i+1][j] == '#' and grid[i+2][j] == '#' and grid[i+3][j] == '#' and grid[i+4][j] == '#' and grid[i+5][j] == '#':
                    return True
                if j+5 < len(grid) and grid[i][j+1] == '#' and grid[i][j+2] == '#' and grid[i][j+3] == '#' and grid[i][j+4] == '#' and grid[i][j+5] == '#':
                    return True
                if i+5 < len(grid) and j+5 < len(grid) and grid[i+1][j+1] == '#' and grid[i+2][j+2] == '#' and grid[i+3][j+3] == '#' and grid[i+4][j+4] == '#' and grid[i+5][j+5] == '#':
                    return True
                if i+5 < len(grid) and j-5 >= 0 and grid[i+1][j-1] == '#' and grid[i+2][j-2] == '#' and grid[i+3][j-3] == '#' and grid[i+4][j-4] == '#' and grid[i+5][j-5] == '#':
                    return True
    return False
