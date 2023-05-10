def main():
    a, b, h, m = map(int, input().split())
    import math
    theta = abs((h*60+m)/720*360 - m/60*360)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta))))

if __name__ == '__main__':
    main()