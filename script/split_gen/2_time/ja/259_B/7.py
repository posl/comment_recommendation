def rotate(x,y,d):
    import math
    rad = math.radians(d)
    x_dash = x*math.cos(rad) - y*math.sin(rad)
    y_dash = x*math.sin(rad) + y*math.cos(rad)
    return [x_dash,y_dash]
a,b,d = input().split()
a = float(a)
b = float(b)
d = float(d)
x,y = rotate(a,b,d)
print(x,y)
