def rotate(a, b, d):
    import math
    rad = math.radians(d)
    return a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad)
