def check1(s):
    if s[0] < 'A' or s[0] > 'Z':
        return False
    if s[-1] < 'A' or s[-1] > 'Z':
        return False
    return True
