def main():
    w, h, x, y = map(int, input().split())
    s = w * h / 2
    if x == w / 2 and y == h / 2:
        print(s, 1)
    else:
        print(s, 0)
