def cal_abs_max(l):
    l = sorted(l, key=abs, reverse=True)
    return sum(l[:3])
