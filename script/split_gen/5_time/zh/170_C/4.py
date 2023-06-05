def find_nearest_value(x, p_list):
    """找到列表p_list中最接近x的值"""
    p_list.sort()
    if x < p_list[0]:
        return p_list[0]
    elif x > p_list[-1]:
        return p_list[-1]
    else:
        for i in range(len(p_list)):
            if x < p_list[i]:
                if x - p_list[i - 1] < p_list[i] - x:
                    return p_list[i - 1]
                else:
                    return p_list[i]
            elif x == p_list[i]:
                return x
