def get_score(x):
    if x >= 0 and x < 40:
        return 40 - x
    elif x >= 40 and x < 70:
        return 70 - x
    elif x >= 70 and x < 90:
        return 90 - x
    else:
