def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2
    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2
    x3 = (y2 - y1) * (-1) + x1
    y3 = (x1 - x2) + y1
    print(x3, y3)

if __name__ == '__main__':
    main()