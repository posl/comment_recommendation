def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()