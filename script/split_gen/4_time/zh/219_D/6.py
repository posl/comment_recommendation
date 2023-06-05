def get_min_box_num(box_num, x, y, a, b):
    min_box_num = 9999999
    for i in range(box_num):
        if a[i] >= x and b[i] >= y:
            min_box_num = min(min_box_num, i+1)
    return min_box_num
