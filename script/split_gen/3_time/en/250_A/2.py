def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(2 * (h - 1) + 2 * (w - 1) - (r == 1) - (r == h) - (c == 1) - (c == w))
