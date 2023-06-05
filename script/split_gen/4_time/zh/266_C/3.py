def check_convex(a, b, c, d):
    # 1. check cross product
    # 2. check inner product
    # 3. check area
    # 4. check angle
    # 1. check cross product
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1
    def inner_product(x1, y1, x2, y2):
        return x1 * x2 + y1 * y2
    def area(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    def angle(x1, y1, x2, y2, x3, y3):
        return inner_product(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
    # 1. check cross product
    a1 = cross_product(b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1])
    a2 = cross_product(b[0] - a[0], b[1] - a[1], d[0] - a[0], d[1] - a[1])
    b1 = cross_product(d[0] - c[0], d[1] - c[1], a[0] - c[0], a[1] - c[1])
    b2 = cross_product(d[0] - c[0], d[1] - c[1], b[0] - c[0], b[1] - c[1])
    if a1 * a2 < 0 and b1 * b2 < 0:
        return False
    # 2. check inner product
    if inner_product(b[0] - a[0], b[1] - a[1], d[0] - c[0], d[1] - c[1]) > 0:
        return False
    if inner_product(c[0] - b[0], c[1] - b[1], a[0
