def replace_string(s):
    s = list(s)
    for i in range(1,len(s)-1):
        if s[i] == ',' and s[i-1] == '"' and s[i+1] == '"':
            s[i] = '.'
    return ''.join(s)
