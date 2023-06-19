def line(x1,y1,x2,y2,x3,y3):
    if x1==x2==x3:
        return True
    elif y1==y2==y3:
        return True
    elif x1==x2 and x2==x3:
        return True
    elif y1==y2 and y2==y3:
        return True
    elif (y1-y2)/(x1-x2)==(y2-y3)/(x2-x3):
        return True
    else:
        return False
