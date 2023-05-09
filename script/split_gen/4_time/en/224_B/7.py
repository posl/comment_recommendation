def check_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(i+1, len(grid)):
                for l in range(j+1, len(grid[0])):
                    if(grid[i][j]+grid[k][l] > grid[i][l]+grid[k][j]):
                        return False
    return True
