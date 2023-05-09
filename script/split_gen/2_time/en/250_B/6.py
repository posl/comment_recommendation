def get_tile(N, A, B):
    tile = [['.' for i in range(B)] for j in range(A)]
    for i in range(A):
        for j in range(B):
            if (i + j) % 2 == 0:
                tile[i][j] = '#'
    return tile
