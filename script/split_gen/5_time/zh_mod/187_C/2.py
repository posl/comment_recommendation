def check(s):
    if s[0] == '!':
        if s[1:] in dict:
            return True
        else:
            return False
    else:
        if '!'+s in dict:
            return True
        else:
            return False
