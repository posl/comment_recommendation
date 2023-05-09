def rotate_point(x, y, p):
    import math
    p = math.radians(p)
    return x * math.cos(p) - y * math.sin(p), x * math.sin(p) + y * math.cos(p)
