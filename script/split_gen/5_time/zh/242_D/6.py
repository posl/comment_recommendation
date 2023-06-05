def get_next(S):
    next = [0] * len(S)
    next[0] = -1
    i = 0
    j = -1
    while i < len(S) - 1:
        if j == -1 or S[i] == S[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next
