def rotation(a,b,d):
    import math
    a1 = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
    b1 = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))
    return a1,b1
