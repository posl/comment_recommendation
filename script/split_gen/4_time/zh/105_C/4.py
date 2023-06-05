def get_base_minus_2(n):
    if n == 0:
        return 0
    else:
        return n % (-2) + 10 * get_base_minus_2(-(n - n % (-2)) // 2)
