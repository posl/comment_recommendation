def swap(a, b, s):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
