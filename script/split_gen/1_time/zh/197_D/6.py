def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0+x2)/2
    y1 = (y0+y2)/2
    x3 = x1 - y0 + y1
    y3 = y1 + x0 - x1
    x4 = x3 - x0 + x2
    y4 = y3 - y0 + y2
    print(x3, y3)
    print(x4, y4)
