def get_xy(n, x0, y0, x1, y1):
    x2 = (x0 + x1) / 2.0
    y2 = (y0 + y1) / 2.0
    x3 = x2 + (y1 - y0) * ((3 ** 0.5) / 2.0)
    y3 = y2 - (x1 - x0) * ((3 ** 0.5) / 2.0)
    return x2, y2, x3, y3
n = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2, x3, y3 = get_xy(n, x0, y0, x1, y1)
print(x2, y2)

if __name__ == '__main__':
    get_xy()