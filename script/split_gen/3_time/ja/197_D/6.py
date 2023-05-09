def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = ((n - 2) * x0 + 2 * x1) / (n + 2)
    y2 = ((n - 2) * y0 + 2 * y1) / (n + 2)
    print(x2, y2)
