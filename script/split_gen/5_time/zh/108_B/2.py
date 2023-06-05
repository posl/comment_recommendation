def get_x3_y3_x4_y4(x1,y1,x2,y2):
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x3 - x2 + x1
    y4 = y3 - y2 + y1
    return x3,y3,x4,y4
