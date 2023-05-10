def get_extra_points(x):
    if x <= 39:
        return 40 - x
    elif x <= 69:
        return 70 - x
    elif x <= 89:
        return 90 - x
    return "expert"
