def replace_str(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '"':
            if i % 2 == 0:
                s[i] = '"'
            else:
                s[i] = '.'
    return "".join(s)
