def solve():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2 + (y2 - y0) * (2 ** 0.5)) / 2
    y1 = (y0 + y2 + (x0 - x2) * (2 ** 0.5)) / 2
    print(x1, y1)

if __name__ == '__main__':
    solve()