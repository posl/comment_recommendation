def reverse_string(start, end, string):
    return string[:start] + string[start:end+1][::-1] + string[end+1:]
