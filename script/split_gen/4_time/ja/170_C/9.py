def search_nearest_int(x, p_list):
    min_diff = 100
    for p in p_list:
        diff = abs(x - p)
        if diff < min_diff:
            min_diff = diff
            nearest_int = p
    return nearest_int
