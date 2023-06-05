def main():
    n = int(input())
    x0,y0 = map(int,input().split())
    x1,y1 = map(int,input().split())
    x2 = (x0+x1)/2
    y2 = (y0+y1)/2
    x3 = x0-y0+y2
    y3 = y0+x0-x2
    print(x3,y3)
