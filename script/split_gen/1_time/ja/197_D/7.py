def main():
    import sys
    import math
    input = sys.stdin.readline
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2
    y1 = (y0 + y2) / 2
    print(x1, y1)
