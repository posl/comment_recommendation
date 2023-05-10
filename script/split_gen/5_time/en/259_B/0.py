def rotate(x,y,d):
    x1 = x*math.cos(math.radians(d)) - y*math.sin(math.radians(d))
    y1 = x*math.sin(math.radians(d)) + y*math.cos(math.radians(d))
    return x1,y1
