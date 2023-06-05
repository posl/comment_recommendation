def get_max_value(a, b, c, d):
    max_value = -10000000000
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            if max_value < x - y:
                max_value = x - y
    return max_value
