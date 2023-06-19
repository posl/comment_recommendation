def rotate90(grid):
    return [''.join([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0])-1,-1,-1)]
