def main():
    a,b,d = map(int,input().split())
    from math import cos,sin,pi
    rad = d * pi / 180
    x = a * cos(rad) - b * sin(rad)
    y = a * sin(rad) + b * cos(rad)
    print(x,y)

if __name__ == '__main__':
    main()