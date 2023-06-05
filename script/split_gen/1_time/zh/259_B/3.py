def rotate(a, b, d):
    import math
    rad = (d/180.0)*math.pi
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    return (x,y)
