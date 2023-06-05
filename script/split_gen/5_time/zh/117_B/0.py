def is_polygon(n, l):
    if max(l) < sum(l) - max(l):
        return "是"
    else:
        return "否"
