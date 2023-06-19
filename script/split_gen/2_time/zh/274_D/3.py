def is_90degree(x1,y1,x2,y2,x3,y3):
    if (x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)==0:
        return True
    else:
        return False
