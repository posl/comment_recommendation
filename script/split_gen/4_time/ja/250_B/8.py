def paint_tile(N, A, B):
    tile = [["." for i in range(B*N)] for j in range(A*N)]
    for i in range(A*N):
        for j in range(B*N):
            if i % 2 == 0 and j % 2 == 0:
                tile[i][j] = "#"
            elif i % 2 == 1 and j % 2 == 1:
                tile[i][j] = "#"
    return tile
