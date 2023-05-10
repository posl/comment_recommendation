def replace_char(str, i, j):
    str_list = list(str)
    tmp = str_list[i-1]
    str_list[i-1] = str_list[j-1]
    str_list[j-1] = tmp
    return ''.join(str_list)
