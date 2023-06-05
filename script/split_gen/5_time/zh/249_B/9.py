def isWonderfulString(s):
    if s.islower() or s.isupper():
        return False
    else:
        for i in range(len(s)):
            if s.count(s[i])%2!=0:
                return False
        return True
