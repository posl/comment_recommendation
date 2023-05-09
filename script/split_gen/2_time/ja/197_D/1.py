def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y2 - y0) * (N / 4) ** 0.5
    y1 = (y0 + y2) / 2 + (x0 - x2) * (N / 4) ** 0.5
    print(x1, y1)
