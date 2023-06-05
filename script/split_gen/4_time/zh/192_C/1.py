def g_1(x):
    x_str = str(x)
    x_list = list(x_str)
    x_list.sort(reverse=True)
    return int(''.join(x_list))
