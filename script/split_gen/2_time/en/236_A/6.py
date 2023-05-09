def swap(s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)
