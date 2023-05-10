def main():
    a,b,h,m = map(int,input().split())
    import math
    m = m + 60 * h
    m = m / 60
    m = m * 360 / 12
    h = 360 / 12 * h
    h = h + 360 / 12 / 60 * m
    #print(h,m)
    rad = abs(h-m)
    if rad > 180:
        rad = 360 - rad
    rad = rad / 180 * math.pi
    ans = a**2 + b**2 - 2*a*b*math.cos(rad)
    ans = ans**0.5
    print(ans)
