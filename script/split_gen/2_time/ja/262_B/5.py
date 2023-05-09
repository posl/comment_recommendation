def comb(n, r):
    if n == r:
        return 1
    elif r == 1:
        return n
    else:
        return comb(n-1, r) + comb(n-1, r-1)
