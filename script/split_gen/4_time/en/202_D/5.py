def comb(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    return comb(n-1, r-1) * n // r
