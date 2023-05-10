def swap(s, a, b):
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return s
