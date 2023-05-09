def combination(n, r):
    if n < r:
        return 0
    elif n == r:
        return 1
    elif r == 1:
        return n
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)
