def round_off(x):
    if x < 0.25:
        return 0
    elif x < 0.75:
        return 0.5
    else:
        return 1
