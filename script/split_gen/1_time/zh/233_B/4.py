def reverse_string(string, start, end):
    """Reverse string from start to end."""
    string = list(string)
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return ''.join(string)
