def getNums(n):
    if n == 0:
        return 1
    else:
        return 2 * getNums(n - 1)
