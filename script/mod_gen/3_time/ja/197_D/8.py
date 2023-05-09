def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1 + (y0 - y1) * (N / 4)) / 2, (y0 + y1 + (x1 - x0) * (N / 4)) / 2)

if __name__ == '__main__':
    main()