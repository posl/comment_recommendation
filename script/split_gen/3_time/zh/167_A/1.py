def func(s,t):
    if len(s) + 1 != len(t):
        return False
    if s + t[-1] == t:
        return True
    else:
        return False
