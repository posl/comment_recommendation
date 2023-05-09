def is_yymm(s):
    if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
        return True
    else:
        return False
