def solve():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) / 12 * 2 * pi
    m = M / 60 * 2 * pi
    d = (A * cos(h) - B * cos(m)) ** 2 + (A * sin(h) - B * sin(m)) ** 2
    print(sqrt(d))
