def swap(S, i, j):
    S = list(S)
    S[i], S[j] = S[j], S[i]
    return ''.join(S)
