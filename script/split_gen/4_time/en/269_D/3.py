def is_adjacent(x1, y1, x2, y2):
    if x1 == x2 and abs(y1 - y2) == 1:
        return True
    if y1 == y2 and abs(x1 - x2) == 1:
        return True
    if x1 - x2 == 1 and y1 - y2 == 1:
        return True
    if x1 - x2 == -1 and y1 - y2 == -1:
        return True
    if x1 - x2 == 1 and y1 - y2 == 0:
        return True
    if x1 - x2 == -1 and y1 - y2 == 0:
        return True
    return False
