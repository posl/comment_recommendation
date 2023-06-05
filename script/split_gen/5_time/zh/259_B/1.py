def rotate(x, y, d):
    d = d/180*3.1415926535897932384626
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1
