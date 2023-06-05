def check(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return True
    return False
