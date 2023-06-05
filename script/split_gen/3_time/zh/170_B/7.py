def check(x, y):
    if x == 1:
        if y == 2:
            return True
        else:
            return False
    elif x == 2:
        if y == 4 or y == 2:
            return True
        else:
            return False
    else:
        return False
