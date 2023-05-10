def solve():
    import sys
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    if x0 == x1:
        print(x0, y1)
    else:
        a = (y1 - y0) / (x1 - x0)
        b = y0 - a * x0
        print((x0**2 + y0**2 - x1**2 - y1**2) / (2 * (x0 - x1)), a * (x0**2 - x1**2) / (2 * (x0 - x1)) + b)

if __name__ == '__main__':
    solve()