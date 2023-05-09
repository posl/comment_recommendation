def is_satisfied(h, w, grid):
    for i in range(h):
        for j in range(w):
            for k in range(i + 1, h):
                for l in range(j + 1, w):
                    if grid[i][j] + grid[k][l] > grid[k][j] + grid[i][l]:
                        return False
    return True
