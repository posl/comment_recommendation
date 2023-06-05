def move_block(H,W,A):
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算需要移动的块数
    move_block = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > ave_block:
                move_block += A[i][j] - ave_block
    return move_block

if __name__ == '__main__':
    move_block()