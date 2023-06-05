def get_min_permutation(s):
    s = list(s)
    s.sort()
    return ''.join(s)
