def main():
    import math
    a,b,h,m = map(int,input().split())
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(30*h-5.5*m))))
