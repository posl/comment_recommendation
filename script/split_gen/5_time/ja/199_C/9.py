def flip(s, a, b):
    return s[b:] + s[a:b] + s[:a]
