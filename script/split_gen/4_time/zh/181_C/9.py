def is_same_line(x1,y1,x2,y2,x3,y3):
    if x1 == x2 and x2 == x3:
        return True
    elif y1 == y2 and y2 == y3:
        return True
    elif x1 == x2 and x2 != x3:
        return False
    elif x1 == x3 and x2 != x3:
        return False
    elif x2 == x3 and x1 != x3:
        return False
    else:
        if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2):
            return True
        else:
            return False
