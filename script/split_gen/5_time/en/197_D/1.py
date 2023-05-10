def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())
    x1 = (x0 + xn2) / 2
    y1 = (y0 + yn2) / 2
    radian = 2 * math.pi / n
    x2 = (x0 - x1) * math.cos(radian) - (y0 - y1) * math.sin(radian) + x1
    y2 = (x0 - x1) * math.sin(radian) + (y0 - y1) * math.cos(radian) + y1
    print("{:.11f} {:.11f}".format(x2, y2))
