def isEightTimes(s):
    if len(s) == 1:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0:
            return True
        elif int(s[1] + s[0]) % 8 == 0:
            return True
        else:
            return False
    else:
        if int(s) % 8 == 0:
            return True
        elif int(s[2] + s[1] + s[0]) % 8 == 0:
            return True
        elif int(s[1] + s[2] + s[0]) % 8 == 0:
            return True
        elif int(s[1] + s[0] + s[2]) % 8 == 0:
            return True
        elif int(s[0] + s[2] + s[1]) % 8 == 0:
            return True
        elif int(s[0] + s[1] + s[2]) % 8 == 0:
            return True
        else:
            return False
s = input()
