def check(s):
    if len(s) < 3 or len(s) > 16:
        return False
    if s in t:
        return False
    return True
