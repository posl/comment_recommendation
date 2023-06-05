def replace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] != '"':
            s[i] = '.'
    return ''.join(s)
