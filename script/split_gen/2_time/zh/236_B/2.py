def my_swap(s, a, b):
    if a > b:
        a, b = b, a
    if a == b:
        return s
    if a == 1:
        return s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
