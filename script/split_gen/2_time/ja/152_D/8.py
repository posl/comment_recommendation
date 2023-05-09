def count (n):
    if n < 10:
        return 1
    else:
        return 10 * count(n // 10) + 8 * 9 * (n // 10 - 1)
