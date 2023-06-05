def exchange(s, a, b):
    if a < b:
        return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else:
        return s[:b] + s[a] + s[b+1:a] + s[b] + s[a+1:]
