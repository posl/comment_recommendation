def is_convex_polygon(x1, y1, x2, y2, x3, y3, x4, y4):
    is_convex = True
    if (x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2) < 0:
        is_convex = False
    if (x2 - x3) * (y4 - y3) - (y2 - y3) * (x4 - x3) < 0:
        is_convex = False
    if (x3 - x4) * (y1 - y4) - (y3 - y4) * (x1 - x4) < 0:
        is_convex = False
    if (x4 - x1) * (y2 - y1) - (y4 - y1) * (x2 - x1) < 0:
        is_convex = False
    return is_convex

if __name__ == '__main__':
    is_convex_polygon()