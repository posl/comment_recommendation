def reverse_string(s, start, end):
    return s[:start-1] + s[start-1:end][::-1] + s[end:]
