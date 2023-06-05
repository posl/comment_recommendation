def isMonth(s):
    if s[0] == '0':
        return False
    elif s[0] == '1':
        if ord(s[1]) >= ord('0') and ord(s[1]) <= ord('2'):
            return True
        else:
            return False
    elif s[0] == '2':
        if ord(s[1]) >= ord('0') and ord(s[1]) <= ord('2'):
            return True
        else:
            return False
    else:
        return False
