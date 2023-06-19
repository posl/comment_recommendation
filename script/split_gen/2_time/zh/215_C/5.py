def permutation(s, k):
    s = sorted(s)
    return ''.join(s[k-1])
