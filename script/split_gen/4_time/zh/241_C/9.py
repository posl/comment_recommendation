def check_grid(grid, N):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                if i+5 < N and grid[i+1][j] == '#' and grid[i+2][j] == '#' and grid[i+3][j] == '#' and grid[i+4][j] == '#' and grid[i+5][j] == '#':
                    return True
                if j+5 < N and grid[i][j+1] == '#' and grid[i][j+2] == '#' and grid[i][j+3] == '#' and grid[i][j+4] == '#' and grid[i][j+5] == '#':
                    return True
                if i+5 < N and j+5 < N and grid[i+1][j+1] == '#' and grid[i+2][j+2] == '#' and grid[i+3][j+3] == '#' and grid[i+4][j+4] == '#' and grid[i+5][j+5] == '#':
                    return True
                if i+5 < N and j-5 >= 0 and grid[i+1][j-1] == '#' and grid[i+2][j-2] == '#' and grid[i+3][j-3] == '#' and grid[i+4][j-4] == '#' and grid[i+5][j-5] == '#':
                    return True
    return False
