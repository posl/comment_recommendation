def main():
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    if (x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()