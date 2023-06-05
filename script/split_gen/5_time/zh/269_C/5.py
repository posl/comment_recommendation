def check(n, x):
    while n > 0:
        if n & 1 == 1 and x & 1 == 0:
            return False
        n >>= 1
        x >>= 1
    return True
