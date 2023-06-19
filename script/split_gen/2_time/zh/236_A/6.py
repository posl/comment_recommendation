def swap_char(s, a, b):
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
