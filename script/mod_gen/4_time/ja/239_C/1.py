def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
        return
    if (x1 + y1) == (x2 + y2):
        print('Yes')
        return
    if (x1 - y1) == (x2 - y2):
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()