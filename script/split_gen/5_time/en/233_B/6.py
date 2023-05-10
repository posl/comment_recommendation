def reverse_string(string, start, end):
    string = list(string)
    string[start-1:end] = reversed(string[start-1:end])
    return ''.join(string)
