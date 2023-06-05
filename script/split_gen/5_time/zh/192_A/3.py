def extra_coin(x):
    if x % 100 == 0:
        return 100
    else:
        return 100 - x % 100
