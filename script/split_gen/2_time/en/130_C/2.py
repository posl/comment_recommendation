def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    if x * 2 == w and y * 2 == h:
        print(area, 1)
    else:
        print(area, 0)
