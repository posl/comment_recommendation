def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    dx = x2 - x0
    dy = y2 - y0
    x1 = x0 - dx
    y1 = y0 - dy
    print(x1, y1)

if __name__ == '__main__':
    main()