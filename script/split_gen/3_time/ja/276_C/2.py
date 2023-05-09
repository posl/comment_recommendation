def next_permutation(p):
    n = len(p)
    i = n - 1
    while i > 0 and p[i - 1] >= p[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while p[j] <= p[i - 1]:
        j -= 1
    p[i - 1], p[j] = p[j], p[i - 1]
    j = n - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True
