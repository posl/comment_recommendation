def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print((x2 + (x2 - x0)), (y2 + (y2 - y0)))
