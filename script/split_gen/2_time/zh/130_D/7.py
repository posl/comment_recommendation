def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    print(area, end=' ')
    if 2 * x == w and 2 * y == h:
        print(1)
    else:
        print(0)
