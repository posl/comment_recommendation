def main():
    a, b, h, m = map(int, input().split())
    import math
    x = (h + m / 60) * 30
    y = m * 6
    z = (x - y) % 360
    if z > 180:
        z = 360 - z
    z = math.radians(z)
    print((a ** 2 + b ** 2 - 2 * a * b * math.cos(z)) ** 0.5)

if __name__ == '__main__':
    main()