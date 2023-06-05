def d(n):
    if n < 10:
        return 1
    return 1 + d(n//10)
