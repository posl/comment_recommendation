def get_x1_y1(x0, y0, x2, y2):
    x1 = x0 + (x2 - x0) * 1.0 / 2 - (y2 - y0) * 1.0 / 2 * 3 ** 0.5
    y1 = y0 + (y2 - y0) * 1.0 / 2 + (x2 - x0) * 1.0 / 2 * 3 ** 0.5
    return x1, y1
N = int(input())
x0, y0 = map(int, input().split())
x2, y2 = map(int, input().split())
x1, y1 = get_x1_y1(x0, y0, x2, y2)
print(x1, y1)
