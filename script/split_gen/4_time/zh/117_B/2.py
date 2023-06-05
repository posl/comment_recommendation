def is_polygon(n, l):
    if n < 3 or n > 10:
        return False
    max_l = max(l)
    sum_l = sum(l) - max_l
    if max_l < sum_l:
        return True
    else:
        return False
