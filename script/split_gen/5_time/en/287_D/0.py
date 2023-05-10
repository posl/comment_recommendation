def is_match(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i] and s[i] != '?':
            return False
    return True
