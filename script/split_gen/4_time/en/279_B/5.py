def is_substring(s, t):
    if len(t) > len(s):
        return False
    if s.find(t) >= 0:
        return True
    return False
