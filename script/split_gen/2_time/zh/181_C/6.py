def isLine(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        if x2 == x3:
            return True
        else:
            return False
    elif x2 == x3:
        return False
    elif y1 == y2:
        if y2 == y3:
            return True
        else:
            return False
    elif y2 == y3:
        return False
    elif (y1 - y2) / (x1 - x2) == (y2 - y3) / (x2 - x3):
        return True
    else:
        return False
