def get_min_block(H, W, A):
    min_block = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_block:
                min_block = A[i][j]
    return min_block
