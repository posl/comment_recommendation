def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x = (x0 + x1) / 2
    y = (y0 + y1) / 2
    x2 = (x0 - x1) / (N - 4) + x
    y2 = (y0 - y1) / (N - 4) + y
    print(x2, y2)

if __name__ == '__main__':
    main()