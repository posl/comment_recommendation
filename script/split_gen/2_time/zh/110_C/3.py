def check(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True
