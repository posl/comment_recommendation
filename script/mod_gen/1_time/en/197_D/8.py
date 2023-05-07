def main():
    N = int(input())
    x0, y0 = map(float, input().split())
    x1, y1 = map(float, input().split())
    x2 = x1 + (x1 - x0)
    y2 = y1 + (y1 - y0)
    print(x2, y2)

if __name__ == '__main__':
    main()