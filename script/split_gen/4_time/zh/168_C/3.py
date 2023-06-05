def clock():
    a,b,h,m = map(int, input().split())
    hour = h + m/60
    hour_angle = hour * 30
    minute_angle = m * 6
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    import math
    angle = math.radians(angle)
    c = (a**2 + b**2 - 2*a*b*math.cos(angle))**0.5
    print(c)
clock()
