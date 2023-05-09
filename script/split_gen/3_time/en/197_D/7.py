def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (N/2*x0+xN2)/(N/2+1)
    y1 = (N/2*y0+yN2)/(N/2+1)
    print(x1, y1)
