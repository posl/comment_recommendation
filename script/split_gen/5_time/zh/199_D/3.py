def get_color_num(n, m):
    if n == 1:
        return 3
    else:
        return 3 * get_color_num(n - 1, m) - get_color_num(n - 2, m)
