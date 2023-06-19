def rotate(x, y, d):
    import math
    x2 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y2 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    return x2, y2
