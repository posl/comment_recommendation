def solve(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)
