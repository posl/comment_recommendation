def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = 0,0,0,0
    if x1 == x2:
        if y2 > y1:
            x3,y3 = x1 + (y2 - y1),y1 + (x1 - x2)
            x4,y4 = x2 + (y2 - y1),y2 + (x1 - x2)
        else:
            x3,y3 = x1 + (y1 - y2),y1 + (x1 - x2)
            x4,y4 = x2 + (y1 - y2),y2 + (x1 - x2)
    elif y1 == y2:
        if x2 > x1:
            x3,y3 = x1 + (y1 - y2),y1 + (x2 - x1)
            x4,y4 = x2 + (y1 - y2),y2 + (x2 - x1)
        else:
            x3,y3 = x1 + (y1 - y2),y1 + (x1 - x2)
            x4,y4 = x2 + (y1 - y2),y2 + (x1 - x2)
    else:
        x3,y3 = x1 + (y1 - y2),y1 + (x2 - x1)
        x4,y4 = x2 + (y1 - y2),y2 + (x2 - x1)
    print(x3,y3,x4,y4)

if __name__ == '__main__':
    main()