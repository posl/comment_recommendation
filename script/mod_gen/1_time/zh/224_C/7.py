def get_area(x1,y1,x2,y2,x3,y3):
    return abs(0.5*((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)))

if __name__ == '__main__':
    get_area()