def calc_area(a,b,c):
    a_x = a[0]
    a_y = a[1]
    b_x = b[0]
    b_y = b[1]
    c_x = c[0]
    c_y = c[1]
    area = (a_x*b_y+b_x*c_y+c_x*a_y-a_x*c_y-b_x*a_y-c_x*b_y)/2
    return area
