def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xh, yh = map(int, input().split())
    x1 = (x0 + xh + (yh - y0) * (3 ** 0.5)) / 2
    y1 = (y0 + yh + (x0 - xh) * (3 ** 0.5)) / 2
    print(x1, y1)

if __name__ == '__main__':
    main()