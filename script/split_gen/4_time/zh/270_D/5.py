def cal_max(a, k):
    if k == 0:
        return a
    else:
        return cal_max(a - (a & -a), k - 1)
