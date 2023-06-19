def d(x):
    if x < 10:
        return 1
    else:
        return 1 + d(x // 10)
