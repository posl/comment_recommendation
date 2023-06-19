def get_max_value(v_list):
    if len(v_list) == 1:
        return v_list[0]
    else:
        v_list.sort()
        value = (v_list[0] + v_list[1]) / 2
        v_list[0] = value
        v_list.pop(1)
        return get_max_value(v_list)
