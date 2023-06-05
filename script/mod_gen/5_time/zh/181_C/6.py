def is_line(point1, point2, point3):
    #判断三点是否在一条直线上
    if (point1[0]-point2[0])*(point1[1]-point3[1]) == (point1[0]-point3[0])*(point1[1]-point2[1]):
        return True
    else:
        return False

if __name__ == '__main__':
    is_line()