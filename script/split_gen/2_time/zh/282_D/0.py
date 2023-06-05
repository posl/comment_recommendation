def replace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '"':
            if i % 2 == 0:
                s[i] = '.'
    return "".join(s)
