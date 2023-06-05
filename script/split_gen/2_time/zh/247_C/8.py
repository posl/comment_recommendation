def get_nickname(s,t):
    if len(s) < len(t):
        min_len = len(s)
    else:
        min_len = len(t)
    for i in range(min_len):
        if s[i] != t[i]:
            return s[0:i+1]
    return s[0:min_len+1]
