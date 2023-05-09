def check(grid, n, i, j):
    for k in range(1, 7):
        if i + k >= n or j + k >= n:
            return False
        if grid[i + k][j + k] == '.':
            return False
    return True
