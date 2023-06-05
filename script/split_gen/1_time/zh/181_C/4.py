def isLine(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x1 == x3:
        return True
    elif y1 == y2 and y1 == y3:
        return True
    elif (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
        return True
    else:
        return False
