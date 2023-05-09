def rotate(a, b, d):
    import math
    theta = math.radians(d)
    x = a * math.cos(theta) - b * math.sin(theta)
    y = a * math.sin(theta) + b * math.cos(theta)
    return x, y
