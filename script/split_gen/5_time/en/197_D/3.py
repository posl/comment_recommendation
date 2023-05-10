def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2
    # rotate
    x3 = x0 - x2
    y3 = y0 - y2
    x4 = -y3
    y4 = x3
    # translate
    x5 = x4 + x2
    y5 = y4 + y2
    print(x5, y5)
