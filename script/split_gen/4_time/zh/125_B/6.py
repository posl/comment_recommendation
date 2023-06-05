def max_value(n, v, c):
    max_value = 0
    for i in range(1, 2**n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += v[j]
                cost += c[j]
        if value > cost and value - cost > max_value:
            max_value = value - cost
    return max_value
