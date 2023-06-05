def is_ok(n):
    s = str(n)
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return True
        else:
            return False
