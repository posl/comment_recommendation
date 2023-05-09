def rotate90(grid):
    return [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0])-1, -1, -1)]
