def main():
    N = int(input()) 
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x2 + 2 * x0) / 3
    y1 = (y2 + 2 * y0) / 3
    print(x1, y1)
