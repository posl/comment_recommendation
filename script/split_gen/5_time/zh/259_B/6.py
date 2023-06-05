def rotate(a, b, d):
    from math import sin, cos, radians
    d = radians(d)
    x = a * cos(d) - b * sin(d)
    y = a * sin(d) + b * cos(d)
    return x, y
