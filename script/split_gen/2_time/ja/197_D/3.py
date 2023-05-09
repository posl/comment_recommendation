def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    dx = xN2 - x0
    dy = yN2 - y0
    x1 = x0 - dx
    y1 = y0 - dy
    print(x1, y1)
