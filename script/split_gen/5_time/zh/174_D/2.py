def get_min_op_num(stones):
    white_stone_num = stones.count('W')
    if white_stone_num == 0:
        return 0
    else:
        white_stone_idx = stones.index('W')
        red_stone_idx = stones.rindex('R')
        red_stone_num = stones.count('R')
        if red_stone_idx < white_stone_idx:
            return white_stone_num
        else:
            return red_stone_num - white_stone_num
