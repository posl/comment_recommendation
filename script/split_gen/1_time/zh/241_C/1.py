def get_black_num(grid):
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                num += 1
    return num
