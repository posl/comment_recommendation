def rotate90(grid):
    N = len(grid)
    ret = [['.']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = grid[i][j]
    return ret
