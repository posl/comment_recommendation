def rotate(x, y, p):
    from math import sin, cos, radians
    return x * cos(radians(p)) - y * sin(radians(p)), x * sin(radians(p)) + y * cos(radians(p))
