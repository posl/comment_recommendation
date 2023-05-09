def rotate(x,y,deg):
    import math
    rad = math.radians(deg)
    x1 = x*math.cos(rad) - y*math.sin(rad)
    y1 = x*math.sin(rad) + y*math.cos(rad)
    return x1,y1
x,y,deg = map(int,input().split())
ans = rotate(x,y,deg)
print(ans[0],ans[1])
