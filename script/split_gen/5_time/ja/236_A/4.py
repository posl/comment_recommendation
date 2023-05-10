def problem236a(s, a, b):
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return "".join(s)
