def rotate(x,y,d):
    import math
    rad=math.radians(d)
    x1=x*math.cos(rad)-y*math.sin(rad)
    y1=x*math.sin(rad)+y*math.cos(rad)
    return x1,y1
