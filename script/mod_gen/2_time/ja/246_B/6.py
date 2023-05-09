def main():
    A, B = map(int, input().split())
    # 2点間の距離を求める
    # d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    d = (A ** 2 + B ** 2) ** 0.5
    # 2点間の距離を1にするためには、
    # (x2 - x1) / d
    # (y2 - y1) / d
    # とする
    x = A / d
    y = B / d
    print(x, y)

if __name__ == '__main__':
    main()