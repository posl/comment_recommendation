def clock(a,b,h,m):
    import math
    angle = math.pi/6*h-m*math.pi/30
    return math.sqrt(a**2+b**2-2*a*b*math.cos(angle))
print(clock(3,4,9,0))
print(clock(3,4,10,40))
