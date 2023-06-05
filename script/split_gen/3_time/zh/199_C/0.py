def swap(a, b, s):
    if a < b:
        return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    else:
        return s[:b-1] + s[a-1] + s[b:a-1] + s[b-1] + s[a:]
