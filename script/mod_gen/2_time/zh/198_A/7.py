def solve():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (2*xN2 - x0) / 2
    y1 = (2*yN2 - y0) / 2
    print(x1, y1)

if __name__ == '__main__':
    solve()