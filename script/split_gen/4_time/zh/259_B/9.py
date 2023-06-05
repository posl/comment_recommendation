def rota(a,b,d):
    import math
    d1 = math.radians(d)
    x = a * math.cos(d1) - b * math.sin(d1)
    y = a * math.sin(d1) + b * math.cos(d1)
    return x,y
a,b,d = map(int,input().split())
x,y = rota(a,b,d)
print(x,y)
