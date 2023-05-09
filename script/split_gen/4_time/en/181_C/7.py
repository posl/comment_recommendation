def isLine(x1,y1,x2,y2,x3,y3):
    if (x1==x2 and x2==x3) or (y1==y2 and y2==y3):
        return True
    elif (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return True
    else:
        return False
