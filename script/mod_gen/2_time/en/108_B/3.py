def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    print(x2 - dy, y2 + dx, x1 - dy, y1 + dx)

if __name__ == '__main__':
    main()