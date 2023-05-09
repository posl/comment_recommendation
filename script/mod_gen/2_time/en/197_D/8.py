def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1) / 2 + (y0 - y1) / (2 * n), (y0 + y1) / 2 + (x1 - x0) / (2 * n))

if __name__ == '__main__':
    main()