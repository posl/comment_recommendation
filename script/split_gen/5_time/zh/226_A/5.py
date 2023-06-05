def round_up(x):
    if x < 0.25:
        return 0
    elif 0.25 <= x < 0.75:
        return 0.5
    else:
        return 1
