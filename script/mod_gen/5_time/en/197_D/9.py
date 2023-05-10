def solve(n, x0, y0, x1, y1):
    x2 = (x0 + x1 + (y0 - y1) * (3 ** 0.5)) / 2
    y2 = (y0 + y1 + (x1 - x0) * (3 ** 0.5)) / 2
    return x2, y2

if __name__ == '__main__':
    solve()