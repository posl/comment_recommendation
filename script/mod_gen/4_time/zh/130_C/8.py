def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    if 2 * x == w and 2 * y == h:
        print(area, 1)
    else:
        print(area, 0)

if __name__ == '__main__':
    main()