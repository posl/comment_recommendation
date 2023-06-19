def is_distance_5(x1, y1, x2, y2):
    if (x1 == x2 and y1 == y2):
        return False
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) == 5:
        return True
    else:
        return False
