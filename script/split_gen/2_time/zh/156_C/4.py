def cal_min(x, n):
    min = 0
    for i in range(n):
        min += (x - i) ** 2
    return min
