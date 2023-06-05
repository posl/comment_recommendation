def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] or t[i] == t[i + 1]:
            return False
    return True
