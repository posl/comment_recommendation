def check_polygon(n, l):
    max_l = max(l)
    sum_l = sum(l) - max_l
    if max_l < sum_l:
        return "是"
    else:
        return "否"
