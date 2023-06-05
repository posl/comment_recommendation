def is_slope_in_1_to_minus1(x1,y1,x2,y2):
    return abs((y2-y1)/(x2-x1))<=1

if __name__ == '__main__':
    is_slope_in_1_to_minus1()