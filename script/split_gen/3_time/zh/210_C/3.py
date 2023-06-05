def max_color_num(a, k):
    """
    :param a: list
    :param k: int
    :return: int
    """
    if len(a) <= k:
        return len(set(a))
    else:
        max_color = 0
        for i in range(len(a) - k + 1):
            max_color = max(max_color, len(set(a[i:i+k])))
        return max_color
