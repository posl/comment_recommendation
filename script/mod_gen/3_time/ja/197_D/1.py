def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y2 - y0) / (2 * N)
    y1 = (y0 + y2) / 2 + (x0 - x2) / (2 * N)
    print(x1, y1)

if __name__ == '__main__':
    main()