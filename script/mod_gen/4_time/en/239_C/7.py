def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = (x1 + x2 + y1 - y2) // 2
    y3 = (x1 + y2 - x2 + y1) // 2
    x4 = (x1 + x2 - y1 + y2) // 2
    y4 = (-x1 + x2 + y1 + y2) // 2
    if (x1 - x3) ** 2 + (y1 - y3) ** 2 == (x1 - x4) ** 2 + (y1 - y4) ** 2 and (x2 - x3) ** 2 + (y2 - y3) ** 2 == (x2 - x4) ** 2 + (y2 - y4) ** 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()