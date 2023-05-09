def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    multiple = 0
    if x == w / 2 and y == h / 2:
        multiple = 1
    print(area, multiple)

if __name__ == '__main__':
    main()