def rotate(a,b,d):
    import math
    a1=a*math.cos(math.radians(d))-b*math.sin(math.radians(d))
    b1=a*math.sin(math.radians(d))+b*math.cos(math.radians(d))
    return a1,b1
a,b,d=map(int,input().split())
a1,b1=rotate(a,b,d)
print(a1,b1)
