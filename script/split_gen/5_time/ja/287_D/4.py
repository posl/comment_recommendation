def check(s, t, x):
    for i in range(x):
        if s[i] != '?' and s[i] != t[i]:
            return False
    for i in range(len(t)):
        if s[i+x] != '?' and s[i+x] != t[i]:
            return False
    return True
