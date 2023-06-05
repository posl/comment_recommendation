def is_polygon(n, l):
    max_l = max(l)
    if max_l < sum(l) - max_l:
        return "是"
    else:
        return "否"
