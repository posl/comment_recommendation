def check(s, t):
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            return True
    return False
