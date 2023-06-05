def check(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    if s[0] == t[0]:
        return check(s[1:], t[1:])
    if s[-1] == t[-1]:
        return check(s[:-1], t[:-1])
    return False
