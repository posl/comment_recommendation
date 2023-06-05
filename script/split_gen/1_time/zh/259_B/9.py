def rotate(x,y,d):
    import math
    d = math.radians(d)
    x_ = x*math.cos(d) - y*math.sin(d)
    y_ = x*math.sin(d) + y*math.cos(d)
    return x_,y_
