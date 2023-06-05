def split_num(n):
    n_str = str(n)
    n_len = len(n_str)
    n_list = []
    for i in range(n_len):
        for j in range(i+1, n_len):
            n_list.append([int(n_str[:i+1]), int(n_str[i+1:j+1])])
    return n_list
