def get_min_str(str):
    str_list = list(str)
    str_list.sort()
    return "".join(str_list)

if __name__ == '__main__':
    get_min_str()