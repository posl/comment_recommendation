def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = x0 + x1 - x0
    y2 = y0 + y1 - y0
    print(x2, y2)
