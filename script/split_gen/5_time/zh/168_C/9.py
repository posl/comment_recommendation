def clock(a,b,h,m):
    if h > 12:
        h = h - 12
    h = h + m/60
    h = h * 30
    m = m * 6
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.1415926535897932384626433832795 / 180
    c = a**2 + b**2 - 2*a*b * math.cos(angle)
    c = math.sqrt(c)
    return c
import math
a,b,h,m = map(int,input().split())
print(clock(a,b,h,m))
