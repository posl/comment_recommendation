def main():
    a,b,h,m = map(int, input().split())
    import math
    x = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(abs(30*h-5.5*m))))
    print(x)
