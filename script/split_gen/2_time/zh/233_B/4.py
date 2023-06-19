def reverse_string(s, start, end):
    s[start:end+1] = list(reversed(s[start:end+1]))
    return s
