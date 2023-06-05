def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)
