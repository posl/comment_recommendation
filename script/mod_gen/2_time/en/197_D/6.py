def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = x0 + x2 - y0 + y2
    y1 = y0 + x2 - x0 + y2
    print(x1, y1)

if __name__ == '__main__':
    main()