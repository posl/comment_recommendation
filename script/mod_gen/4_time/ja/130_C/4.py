def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    print(area, 1 if x * 2 == w and y * 2 == h else 0)

if __name__ == '__main__':
    main()