def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) - y0 + y2
    y1 = (y0 + y2) - x2 + x0
    print(x1, y1)
