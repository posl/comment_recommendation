def get_max_sum(a, b):
    max_sum = 0
    for i in range(len(b)):
        if i == 0:
            max_sum += b[i]
        else:
            max_sum += min(b[i], b[i-1])
    return max_sum
