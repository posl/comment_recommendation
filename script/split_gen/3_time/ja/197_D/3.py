def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = 2 * x2 - x0
    y1 = 2 * y2 - y0
    print(x1, y1)
