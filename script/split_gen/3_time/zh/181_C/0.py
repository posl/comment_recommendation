def isLine(points):
    if len(points) < 3:
        return False
    if len(points) == 3:
        return True
    x1, y1 = points[0]
    x2, y2 = points[1]
    if x1 == x2:
        k = 'x'
    else:
        k = (y2 - y1) / (x2 - x1)
    for i in range(2, len(points)):
        x, y = points[i]
        if k != 'x' and k != (y - y1) / (x - x1):
            return False
        elif k == 'x' and x != x1:
            return False
    return True
