def replace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] = 'b'
        elif s[i] == 'b':
            s[i] = 'c'
        else:
            s[i] = 'a'
    return ''.join(s)
