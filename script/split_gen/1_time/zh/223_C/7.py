def get_distance(a, b, n):
    """
    二分法
    :param a: a
    :param b: b
    :param n: n
    :return: distance
    """
    left = 0
    right = 1000
    while left < right:
        mid = (left + right) / 2
        sum = 0
        for i in range(n):
            sum += a[i] / (mid - b[i])
        if sum < 1:
            right = mid
        else:
            left = mid
    return left
