def replace_str(s):
    s = list(s)
    for i in range(len(s)-1):
        if s[i] == 'n' and s[i+1] == 'a':
            s[i] = 'n'
            s[i+1] = 'y'
    return ''.join(s)
