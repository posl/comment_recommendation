def problems259_b(a, b, d):
    import math
    d = math.radians(d)
    a1 = a * math.cos(d) - b * math.sin(d)
    b1 = a * math.sin(d) + b * math.cos(d)
    return a1, b1
