def calc_internal_rating(n, r):
    if n < 10:
        return r + 100 * (10 - n)
    else:
        return r
