def l(x):
    if x == 0:
        return 0
    elif x < 10:
        return 1
    else:
        return 1 + l(x // 10)
