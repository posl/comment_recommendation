def is_convex(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2 == x3 == x4 or y1 == y2 == y3 == y4:
        return False
    if (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2):
        return False
    if (x1 - x2) * (y1 - y4) == (x1 - x4) * (y1 - y2):
        return False
    if (x1 - x3) * (y1 - y4) == (x1 - x4) * (y1 - y3):
        return False
    if (x2 - x3) * (y2 - y4) == (x2 - x4) * (y2 - y3):
        return False
    return True
