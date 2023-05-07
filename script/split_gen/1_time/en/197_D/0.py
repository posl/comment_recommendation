def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    dx = x1 - x0
    dy = y1 - y0
    x2 = x1 - dy
    y2 = y1 + dx
    print(x2, y2)
