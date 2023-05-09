def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - x1
    y3 = y2 - y1
    x4 = -y3
    y4 = x3
    x5 = x4 + x1
    y5 = y4 + y1
    x6 = x5 + x2
    y6 = y5 + y2
    print(x5, y5, x6, y6)
