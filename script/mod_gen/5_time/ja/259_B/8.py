def main():
    a,b,d = map(int, input().split())
    if d == 0 or d == 360:
        print(a,b)
    elif d == 180:
        print(-a,-b)
    else:
        import math
        x = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
        y = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))
        print(x,y)

if __name__ == '__main__':
    main()