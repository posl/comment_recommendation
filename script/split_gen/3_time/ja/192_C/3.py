def g1(x):
    x_str = str(x)
    x_str_list = list(x_str)
    x_str_list.sort(reverse=True)
    x_str = ''.join(x_str_list)
    return int(x_str)
