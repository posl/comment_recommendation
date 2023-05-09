def next_permutation(p):
    i = len(p) - 2
    while i >= 0 and p[i] >= p[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(p) - 1
    while p[i] >= p[j]:
        j -= 1
    p[i], p[j] = p[j], p[i]
    p[i + 1:] = reversed(p[i + 1:])
    return True
