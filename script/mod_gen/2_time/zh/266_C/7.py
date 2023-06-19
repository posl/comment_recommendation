def isConvex(x1, y1, x2, y2, x3, y3, x4, y4):
    a = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    b = (x3 - x2) * (y4 - y3) - (y3 - y2) * (x4 - x3)
    c = (x4 - x3) * (y1 - y4) - (y4 - y3) * (x1 - x4)
    d = (x1 - x4) * (y2 - y1) - (y1 - y4) * (x2 - x1)
    if a * b < 0 and b * c < 0 and c * d < 0 and d * a < 0:
        return True
    else:
        return False

if __name__ == '__main__':
    isConvex()