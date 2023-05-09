def swap_string(s, a, b):
    a = a - 1
    b = b - 1
    c = s[a]
    s[a] = s[b]
    s[b] = c
    return s
