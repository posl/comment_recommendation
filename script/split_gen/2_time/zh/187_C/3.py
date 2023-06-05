def get_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return 0
    return (y2 - y1) / (x2 - x1)
