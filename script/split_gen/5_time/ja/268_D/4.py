def isMatch(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if t[i] != '_' and s[i] != t[i]:
            return False
    return True
