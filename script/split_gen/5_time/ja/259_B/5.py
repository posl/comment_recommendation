def rotation(x,y,d):
    import math
    rad = d * math.pi / 180
    return (x*math.cos(rad) - y*math.sin(rad), x*math.sin(rad) + y*math.cos(rad))
a,b,d = map(int,input().split())
x,y = rotation(a,b,d)
print(x,y)
