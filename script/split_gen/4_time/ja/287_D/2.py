def check(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True
