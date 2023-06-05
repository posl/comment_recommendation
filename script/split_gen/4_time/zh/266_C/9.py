def isConvex(a, b, c, d):
    # a, b, c, d: (x, y)
    # return: True if the quadrangle is convex, False otherwise
    # WRITE ME!
    a = (b[0] - a[0], b[1] - a[1])
    b = (c[0] - b[0], c[1] - b[1])
    c = (d[0] - c[0], d[1] - c[1])
    d = (a[0] - d[0], a[1] - d[1])
    a = a[0] * b[1] - a[1] * b[0]
    b = b[0] * c[1] - b[1] * c[0]
    c = c[0] * d[1] - c[1] * d[0]
    d = d[0] * a[1] - d[1] * a[0]
    return a * b > 0 and b * c > 0 and c * d > 0
