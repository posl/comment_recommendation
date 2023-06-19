def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False
