def main():
    a,b,h,m = map(int,input().split())
    import math
    x = math.radians(30*h+0.5*m)
    y = math.radians(6*m)
    import math
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(x-y)))
