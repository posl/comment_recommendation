def rotate(x,y,degree):
    degree = degree/180*3.14159265358979323846264338327950288
    x1 = x * math.cos(degree) - y * math.sin(degree)
    y1 = x * math.sin(degree) + y * math.cos(degree)
    return x1,y1
