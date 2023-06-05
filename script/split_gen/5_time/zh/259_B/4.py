def get_new_point(a,b,d):
    import math
    a = float(a)
    b = float(b)
    d = float(d)
    d = math.radians(d)
    x = a*math.cos(d)-b*math.sin(d)
    y = a*math.sin(d)+b*math.cos(d)
    return x,y
