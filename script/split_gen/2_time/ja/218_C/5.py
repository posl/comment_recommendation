def is_same_grid(grid1, grid2):
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
