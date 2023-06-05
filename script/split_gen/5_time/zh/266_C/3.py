def is_convex(x1,y1,x2,y2,x3,y3,x4,y4):
    if (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1) < 0:
        return False
    if (x3-x2)*(y4-y3) - (x4-x3)*(y3-y2) < 0:
        return False
    if (x4-x3)*(y1-y4) - (x1-x4)*(y4-y3) < 0:
        return False
    if (x1-x4)*(y2-y1) - (x2-x1)*(y1-y4) < 0:
        return False
    return True
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = map(int,input().split())
