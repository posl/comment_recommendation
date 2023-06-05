def find_min(str):
    if len(str) == 1:
        return str
    else:
        min_str = str
        for i in range(len(str)):
            str_list = list(str)
            str_list[0], str_list[i] = str_list[i], str_list[0]
            new_str = ''.join(str_list)
            if new_str < min_str:
                min_str = new_str
        return min_str
