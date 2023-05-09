def main():
    import math
    a,b,h,m = map(int,input().split())
    rad = math.pi/2 - (math.pi/6)*h - (math.pi/360)*m
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(rad)))
