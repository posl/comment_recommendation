def main():
    a, b = map(int, input().split())
    h = b - a
    print(int(h * (h - 1) / 2 - a))
