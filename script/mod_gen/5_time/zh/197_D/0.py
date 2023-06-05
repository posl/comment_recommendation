def getPoint(x0, y0, x1, y1, x2, y2):
    x = (x1 + x2 + x0 - y1 + y2) / 2
    y = (y1 + y2 + y0 + x1 - x2) / 2
    return x, y

if __name__ == '__main__':
    getPoint()