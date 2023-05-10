def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if y0 == y2:
        print(x1, y1)
    else:
        x3 = x1 + (x0 - x1) * ((y1 - y2) / (y0 - y2))
        y3 = y1 + (y0 - y1) * ((y1 - y2) / (y0 - y2))
        print(x3, y3)
