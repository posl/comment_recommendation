def is_intersected(x1,y1,r1,x2,y2,r2):
    d = (x1-x2)**2 + (y1-y2)**2
    if (r1-r2)**2 <= d and d <= (r1+r2)**2:
        return True
    else:
        return False
