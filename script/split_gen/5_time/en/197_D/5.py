def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2 + (y0 - yN2) * (3 ** 0.5)) / 2
    y1 = (y0 + yN2 + (xN2 - x0) * (3 ** 0.5)) / 2
    print(x1, y1)
