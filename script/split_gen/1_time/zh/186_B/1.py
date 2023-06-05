def remove_blocks(h, w, blocks):
    # 1. 求出所有块的总数
    blocks_sum = 0
    for row in blocks:
        blocks_sum += sum(row)
    # 2. 求出每个块的平均数
    blocks_avg = blocks_sum // (h * w)
    # 3. 求出所有块的差值
    blocks_diff = 0
    for row in blocks:
        for block in row:
            blocks_diff += abs(block - blocks_avg)
    # 4. 求出所有块的差值之和
    return blocks_diff
