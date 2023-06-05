def swap_char(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list) - 1):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
        if s_list == t_list:
            return True
        else:
            s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
    return False
