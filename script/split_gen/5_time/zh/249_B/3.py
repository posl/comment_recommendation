def isWonderful(s):
    if s.islower() or s.isupper() or len(s) % 2 == 1:
        return False
    else:
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                return False
        return True
