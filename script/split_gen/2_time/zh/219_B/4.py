def get_level(x):
    if x < 40:
        return 40
    elif x < 70:
        return 70
    elif x < 90:
        return 90
    else:
        return 'expert'
