def main():
    from math import sin, cos, radians
    a, b, d = map(int, input().split())
    x = a * cos(radians(d)) - b * sin(radians(d))
    y = a * sin(radians(d)) + b * cos(radians(d))
    print(x, y)

if __name__ == '__main__':
    main()