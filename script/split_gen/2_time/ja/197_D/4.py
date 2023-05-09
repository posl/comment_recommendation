def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = x0 + (x2 - x0) * (n / 4 - 1) / (n / 2 - 1)
    y1 = y0 + (y2 - y0) * (n / 4 - 1) / (n / 2 - 1)
    print(x1, y1)
