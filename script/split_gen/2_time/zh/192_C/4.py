def g_1(x):
    x_list = list(str(x))
    x_list.sort(reverse=True)
    return int("".join(x_list))
