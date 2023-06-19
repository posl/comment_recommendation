def check(s):
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            return False
    return True
