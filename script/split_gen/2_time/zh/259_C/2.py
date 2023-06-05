def rotate(x, y, d):
    import math
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    return x * cos - y * sin, x * sin + y * cos
