def get_min_blocks(H, W, A):
    #最小块数
    min_blocks = 0
    #求和
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j]
    #求平均数
    average = sum / (H * W)
    #求最小块数
    for i in range(H):
        for j in range(W):
            if average < A[i][j]:
                min_blocks += A[i][j] - average
    return min_blocks
