def Main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = xN2 + (xN2 - x0) * (N / 4) / (N / 2)
    y1 = yN2 + (yN2 - y0) * (N / 4) / (N / 2)
    print(x1, y1)
