def isPrefix(s, t):
    if s == t:
        return True
    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True
