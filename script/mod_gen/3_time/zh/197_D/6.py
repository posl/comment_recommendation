def solve():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2
    x3 = (x0 - x1) * 0.5 * 0.8660254037844386 + (y0 - y1) * 0.5 * 0.5 + x2
    y3 = (y0 - y1) * 0.5 * 0.8660254037844386 - (x0 - x1) * 0.5 * 0.5 + y2
    print(x3, y3)

if __name__ == '__main__':
    solve()