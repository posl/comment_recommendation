def check(s,t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s==t:
        return True
    else:
        return False
