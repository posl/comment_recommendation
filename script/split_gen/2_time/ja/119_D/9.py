def calc_dist(x, s, t):
    if x < s:
        return s - x
    elif t < x:
        return x - t
    else:
        return 0
