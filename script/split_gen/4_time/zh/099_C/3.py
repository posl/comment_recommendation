def cal_min_num(N):
    min_num = 0
    while N > 0:
        if N >= 729:
            N -= 729
            min_num += 1
        elif N >= 81:
            N -= 81
            min_num += 1
        elif N >= 9:
            N -= 9
            min_num += 1
        elif N >= 36:
            N -= 36
            min_num += 1
        elif N >= 6:
            N -= 6
            min_num += 1
        elif N >= 1:
            N -= 1
            min_num += 1
    return min_num
