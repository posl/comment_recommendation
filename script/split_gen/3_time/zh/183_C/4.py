def get_path_num(N, K, T):
    path_num = 0
    for i in range(1, N):
        path_num += get_path_num_from_i(N, K, T, i)
    return path_num
