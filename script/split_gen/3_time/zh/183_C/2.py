def get_path_sum(path, T):
    path_sum = 0
    for i in range(len(path) - 1):
        path_sum += T[path[i]][path[i + 1]]
    return path_sum
