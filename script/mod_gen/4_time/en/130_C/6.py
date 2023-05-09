def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    ans = 0
    if x == w / 2 and y == h / 2:
        ans = 1
    print(area, ans)

if __name__ == '__main__':
    main()