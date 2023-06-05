def main():
    import math
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        ans = math.atan((b*b*a)/(2*x))
    else:
        ans = math.atan((2*b - (2*x)/(a*a)) / a)
    print(math.degrees(ans))
