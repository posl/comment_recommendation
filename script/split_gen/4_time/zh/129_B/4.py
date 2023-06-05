def get_min_weight_diff(n, w):
    min_diff = 1000000000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        if abs(s1 - s2) < min_diff:
            min_diff = abs(s1 - s2)
    return min_diff
