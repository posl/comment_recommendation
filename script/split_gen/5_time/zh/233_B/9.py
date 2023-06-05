def reverse_string(string, begin, end):
    return string[:begin] + string[begin:end+1][::-1] + string[end+1:]
