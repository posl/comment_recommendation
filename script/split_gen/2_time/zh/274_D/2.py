def is90(x1, y1, x2, y2, x3, y3):
    x1 = x1 - x2
    y1 = y1 - y2
    x3 = x3 - x2
    y3 = y3 - y2
    if x1*x3 + y1*y3 == 0:
        return True
    else:
        return False
