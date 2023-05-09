def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2) / 2
    y1 = (y0 + yN2) / 2
    x2 = (x0 - xN2) / 2
    y2 = (y0 - yN2) / 2
    theta = 2 * math.pi / N
    x3 = x2 * math.cos(theta) - y2 * math.sin(theta)
    y3 = x2 * math.sin(theta) + y2 * math.cos(theta)
    x1 = x1 + x3
    y1 = y1 + y3
    print(x1, y1)

if __name__ == '__main__':
    solve()