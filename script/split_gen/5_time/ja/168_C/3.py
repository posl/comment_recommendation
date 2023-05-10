def problem168_c():
    a,b,h,m = map(int,input().split())
    import math
    ang = abs((h*30+m*0.5)-(m*6))
    if ang > 180:
        ang = 360-ang
    ans = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(ang)))
    print(ans)
