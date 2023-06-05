def find_near_num(x, p_list):
    near_num = 0
    near_num_diff = 100
    for i in range(0, 101):
        if i in p_list:
            continue
        if abs(x - i) < near_num_diff:
            near_num_diff = abs(x - i)
            near_num = i
    return near_num
