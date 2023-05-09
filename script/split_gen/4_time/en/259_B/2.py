def rotate(a, b, d):
    import math
    rad = math.radians(d)
    a_dash = a * math.cos(rad) - b * math.sin(rad)
    b_dash = a * math.sin(rad) + b * math.cos(rad)
    return a_dash, b_dash
