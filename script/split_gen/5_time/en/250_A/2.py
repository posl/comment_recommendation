def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h * w) - ((h - r) * w) - ((w - c) * r) + ((h - r) * (w - c)))
