def count(n):
    if n == 0:
        return 1
    return n * count(n-1)
