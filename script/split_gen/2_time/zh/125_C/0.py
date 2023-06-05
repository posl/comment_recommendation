def get_max_value(n, values, costs):
    max_value = 0
    for i in range(2**n):
        value = 0
        cost = 0
        for j in range(n):
            if i & (1 << j):
                value += values[j]
                cost += costs[j]
        if value - cost > max_value:
            max_value = value - cost
    return max_value
