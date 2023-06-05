def d(n):
    if n == 0:
        return 0
    else:
        return n % 10 + d(n // 10)
