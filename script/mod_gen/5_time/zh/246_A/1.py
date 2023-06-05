def get_coordinate():
    #get the coordinate of the point
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    #get the coordinate of the forth point
    x4 = x2 + x3 - x1
    y4 = y2 + y3 - y1
    print(x4,y4)

if __name__ == '__main__':
    get_coordinate()