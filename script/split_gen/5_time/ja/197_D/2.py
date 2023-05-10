def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN, yN = map(int, input().split())
    x1 = (x0+xN)/2 + (y0-yN)*3.0**0.5/2
    y1 = (y0+yN)/2 + (xN-x0)*3.0**0.5/2
    print(x1, y1)
