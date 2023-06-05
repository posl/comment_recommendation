def isbit(x):
    if x == 0:
        return 0
    else:
        return (x & 1) + isbit(x >> 1)
