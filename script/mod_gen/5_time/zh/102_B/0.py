def get_max_abs_diff(a_list):
    a_list.sort()
    return a_list[-1] - a_list[0]

if __name__ == '__main__':
    get_max_abs_diff()