def rotate(x,y,d):
    import math
    d = math.radians(d)
    x = x * math.cos(d) - y * math.sin(d)
    y = x * math.sin(d) + y * math.cos(d)
    return x,y
a,b,d = map(int,input().split())
x,y = rotate(a,b,d)
print(x,y)
