def get_kth_smallest_integer(k):
    if k <= 2:
        return 2 * k
    else:
        return 10 * get_kth_smallest_integer(k - 2) + 2
