def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2
    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2
    import math
    x3 = x2 * math.cos(2 * math.pi / N) - y2 * math.sin(2 * math.pi / N)
    y3 = x2 * math.sin(2 * math.pi / N) + y2 * math.cos(2 * math.pi / N)
    print(x3 + x1, y3 + y1)

if __name__ == '__main__':
    main()