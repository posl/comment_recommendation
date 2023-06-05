def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4 = x3 + x1 - x2
    y4 = y3 + y1 - y2
    print(x4,y4)
