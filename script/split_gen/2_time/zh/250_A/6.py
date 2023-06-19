def get_num_of_same_edge_squares(h,w,r,c):
    num = 0
    if r == 1 and c == 1:
        num = 0
    elif r == 1 and c == w:
        num = 0
    elif r == h and c == 1:
        num = 0
    elif r == h and c == w:
        num = 0
    elif r == 1:
        num = 1
    elif r == h:
        num = 1
    elif c == 1:
        num = 1
    elif c == w:
        num = 1
    else:
        num = 2
    return num
