def get_max_sum(a, b, c):
    """
    获取两个数的最大和
    :param a:
    :param b:
    :param c:
    :return:
    """
    max_sum = 0
    if a > b and a > c:
        max_sum = a + max(b, c)
    elif b > a and b > c:
        max_sum = b + max(a, c)
    elif c > a and c > b:
        max_sum = c + max(a, b)
    else:
        max_sum = a + b
    return max_sum
