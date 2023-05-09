def check_rotation(p1, p2, p3):
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p2[0]
    y2 = p3[1] - p2[1]
    return x1 * y2 - x2 * y1
