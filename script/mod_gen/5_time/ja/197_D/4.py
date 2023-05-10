def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = 0, 0
    x3, y3 = 0, 0
    if x0 == x1:
        x2 = x0 + abs(y0 - y1)
        x3 = x1 + abs(y0 - y1)
    elif y0 == y1:
        y2 = y0 + abs(x0 - x1)
        y3 = y1 + abs(x0 - x1)
    else:
        x2 = x0 + abs(y0 - y1)
        x3 = x1 + abs(y0 - y1)
        y2 = y0 + abs(x0 - x1)
        y3 = y1 + abs(x0 - x1)
    print(x2, y2)

if __name__ == '__main__':
    main()