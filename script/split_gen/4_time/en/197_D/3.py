def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())
    x1 = (x0 + xn2 + (y0 - yn2) * (3 ** 0.5)) / 2
    y1 = (y0 + yn2 + (xn2 - x0) * (3 ** 0.5)) / 2
    print(x1, y1)
