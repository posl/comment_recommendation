def isDouble(s):
    if len(s) % 2 == 1:
        return False
    else:
        if s[0:len(s)/2] == s[len(s)/2:]:
            return True
        else:
            return False
