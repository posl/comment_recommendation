def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1 + (y0 - y1) * 2 ** 0.5) / 2
    y2 = (y0 + y1 + (x1 - x0) * 2 ** 0.5) / 2
    print(x2, y2)
