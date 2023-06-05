def replace_string(string, replace_char, start, end):
    if start >= end:
        return string
    else:
        return string[0:start] + replace_char * (end - start) + string[end:]
