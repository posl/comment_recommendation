def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    print((x0 + x1) / 2 + (y0 - y1) * (N / 4) / (N / 2), (y0 + y1) / 2 + (x1 - x0) * (N / 4) / (N / 2))
