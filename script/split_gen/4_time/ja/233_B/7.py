def reverse_string(s, start, end):
    left = s[:start-1]
    middle = s[start-1:end]
    right = s[end:]
    middle = middle[::-1]
    return left + middle + right
