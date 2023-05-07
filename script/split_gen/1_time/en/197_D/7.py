def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x1 - x0) * (n / 4) + x0, (y1 - y0) * (n / 4) + y0)
