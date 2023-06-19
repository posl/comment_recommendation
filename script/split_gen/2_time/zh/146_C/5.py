def d(n):
    if n < 10:
        return 1
    return d(n//10) + 1
