def combination(n, r):
    if n == 0 or r == 0 or n == r:
        return 1
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)
