def cal_area(ax,ay,bx,by,cx,cy):
    return abs((ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))/2.0)

if __name__ == '__main__':
    cal_area()