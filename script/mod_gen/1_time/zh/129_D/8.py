def get_lighted_cells(wall, H, W, i, j):
    lighted_cells = 0
    for k in range(i, H):
        if wall[k][j] == '#':
            break
        lighted_cells += 1
    for k in range(i, -1, -1):
        if wall[k][j] == '#':
            break
        lighted_cells += 1
    for k in range(j, W):
        if wall[i][k] == '#':
            break
        lighted_cells += 1
    for k in range(j, -1, -1):
        if wall[i][k] == '#':
            break
        lighted_cells += 1
    return lighted_cells - 3

if __name__ == '__main__':
    get_lighted_cells()