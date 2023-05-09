def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    print(area, end=' ')
    if x == w / 2 and y == h / 2:
        print(1)
    else:
        print(0)
