def reverse_string(string, start, end):
    return string[:start] + string[start:end][::-1] + string[end:]
