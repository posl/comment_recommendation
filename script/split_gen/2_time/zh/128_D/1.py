def max_jewel_value(n, k, v):
    max_v = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1 - i):
            v2 = v[:i] + v[-j:]
            v2.sort()
            max_v = max(max_v, sum(v2))
    return max_v
