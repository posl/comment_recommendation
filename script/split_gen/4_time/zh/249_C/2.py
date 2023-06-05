def get_all_combination(src_list, num):
    if num == 0:
        return [[]]
    all_list = []
    for i in range(len(src_list)):
        cur_list = src_list[:i]
        cur_list.extend(src_list[i+1:])
        all_list.extend([[src_list[i]]+x for x in get_all_combination(cur_list, num-1)])
    return all_list
