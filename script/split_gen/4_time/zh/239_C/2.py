def is_5_2(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return False
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        return True
    else:
        return False
