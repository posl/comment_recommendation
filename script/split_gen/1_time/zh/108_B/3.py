def main():
    x1,y1,x2,y2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = x1 - (y2 - y1)
    y3 = y1 - (x1 - x2)
    x4 = x2 - (y2 - y1)
    y4 = y2 - (x1 - x2)
    print(x3,y3,x4,y4)
    return
