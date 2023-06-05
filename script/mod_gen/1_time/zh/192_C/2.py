def g_1(x):
    x_str = str(x)
    x_list = list(x_str)
    x_list.sort(reverse=True)
    x_str = ''.join(x_list)
    return int(x_str)

if __name__ == '__main__':
    g_1()