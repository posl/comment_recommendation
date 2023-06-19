def get_angle(x1,y1,x2,y2):
    if x1==x2:
        return 90
    else:
        return (y2-y1)/(x2-x1)
