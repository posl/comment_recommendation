def next_permutation(p):
    N = len(p)
    for i in range(N - 2, -1, -1):
        if p[i] < p[i + 1]:
            break
    else:
        return False
    for j in range(N - 1, i, -1):
        if p[i] < p[j]:
            break
    p[i], p[j] = p[j], p[i]
    p[i + 1:] = reversed(p[i + 1:])
    return True
