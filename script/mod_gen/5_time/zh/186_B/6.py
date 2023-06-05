def cal_min_block_num(H,W,block_list):
    min_block_num = 10000
    for i in range(H):
        for j in range(W):
            if block_list[i][j] < min_block_num:
                min_block_num = block_list[i][j]
    return min_block_num

if __name__ == '__main__':
    cal_min_block_num()