def rotate90(grid):
    n = len(grid)
    new_grid = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[j][n - i - 1] = grid[i][j]
    return new_grid
