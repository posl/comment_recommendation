def main():
    import math
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(math.atan(a*b*b/2/x)*180/math.pi)
    else:
        print(math.atan((2*b/a-2*x/a/a)*a/b)*180/math.pi)
