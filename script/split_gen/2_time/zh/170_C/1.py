def find_nearest(x, p_list):
    if(len(p_list) == 0):
        return x
    p_list.sort()
    for i in range(len(p_list)):
        if(p_list[i] >= x):
            if(i == 0):
                return p_list[i]
            else:
                return find_nearest(x, [p_list[i-1], p_list[i]])
    return p_list[len(p_list)-1]
