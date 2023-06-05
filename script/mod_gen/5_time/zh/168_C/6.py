def main():
    a, b, h, m = map(int, input().split())
    from math import cos, pi
    print((a**2+b**2-2*a*b*cos((h*60+m)*pi/360))**0.5)

if __name__ == '__main__':
    main()