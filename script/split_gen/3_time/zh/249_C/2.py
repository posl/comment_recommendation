def get_k_str(k, str_list):
    str_list = sorted(str_list, key=lambda x: len(x))
    str_list = str_list[:k]
    str_list = sorted(str_list, key=lambda x: len(set(x)))
    return str_list
