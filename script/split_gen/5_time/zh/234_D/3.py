def max_k_value(p, k):
    max_k = max(p[:k])
    for i in range(k, len(p)):
        if p[i] > max_k:
            max_k = p[i]
    return max_k
