def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    dx = (x1 - x0) / (N / 2)
    dy = (y1 - y0) / (N / 2)
    print(x1 - dy, y1 + dx)
