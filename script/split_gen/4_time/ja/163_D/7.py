def comb(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    if r > n / 2:
        return comb(n, n - r)
    return comb(n, r - 1) * (n - r + 1) // r
