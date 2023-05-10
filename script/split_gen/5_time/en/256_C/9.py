def perm(n, r):
    if n < r:
        return 0
    else:
        return fact(n) // fact(n - r)
