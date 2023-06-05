def g_1(x):
    x_str = str(x)
    x_str_list = list(x_str)
    x_str_list.sort(reverse=True)
    g_1_x = int(''.join(x_str_list))
    return g_1_x
