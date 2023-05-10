def main():
    N = int(input())
    N2 = int(N/2)
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2 + (yN2 - y0) * (2 ** 0.5)) / 2
    y1 = (y0 + yN2 + (x0 - xN2) * (2 ** 0.5)) / 2
    print(x1, y1)
