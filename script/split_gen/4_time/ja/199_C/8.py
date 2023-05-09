def swap(s, a, b):
    s = list(s)
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return "".join(s)
