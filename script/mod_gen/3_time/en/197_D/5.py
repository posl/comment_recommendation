def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = (x0 + x1) / 2, (y0 + y1) / 2
    x3 = x2 - (y2 - y0)
    y3 = y2 + (x2 - x0)
    print(x3, y3)

if __name__ == '__main__':
    main()