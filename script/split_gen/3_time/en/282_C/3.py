def replace_comma(s):
    s = list(s)
    index = 0
    while index < len(s):
        if s[index] == '"':
            index += 1
            while s[index] != '"':
                if s[index] == ',':
                    s[index] = '.'
                index += 1
        index += 1
    return ''.join(s)
