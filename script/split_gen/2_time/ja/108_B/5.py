def solve():
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(x2 - (y2 - y1), y2 + (x2 - x1), x1 - (y2 - y1), y1 + (x2 - x1))
