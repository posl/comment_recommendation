def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    is_multiple = 0
    if w == x * 2 and h == y * 2:
        is_multiple = 1
    print(area, is_multiple)
