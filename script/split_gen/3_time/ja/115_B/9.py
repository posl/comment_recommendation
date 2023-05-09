def calc_price(n, p):
    max_p = max(p)
    p.remove(max_p)
    return sum(p) + max_p / 2
