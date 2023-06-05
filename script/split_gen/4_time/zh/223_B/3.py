def minstr(s):
    s = list(s)
    a = min(s)
    b = s.index(a)
    c = s[:b]
    del s[:b]
    s.extend(c)
    return ''.join(s)
