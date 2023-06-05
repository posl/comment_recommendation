def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        if abs(x1 - x2) + abs(y1 - y2) <= 6:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()