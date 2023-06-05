def isEight(s):
    if len(s) == 1:
        if s == '8':
            return True
        else:
            return False
    if len(s) == 2:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    if len(s) == 3:
        if int(s) % 8 == 0:
            return True
        elif int(s[1] + s[0] + s[2]) % 8 == 0:
            return True
        elif int(s[1] + s[2] + s[0]) % 8 == 0:
            return True
        elif int(s[2] + s[0] + s[1]) % 8 == 0:
            return True
        elif int(s[2] + s[1] + s[0]) % 8 == 0:
            return True
        else:
            return False
    if len(s) == 4:
        if int(s) % 8 == 0:
            return True
        elif int(s[1] + s[0] + s[2] + s[3]) % 8 == 0:
            return True
        elif int(s[1] + s[0] + s[3] + s[2]) % 8 == 0:
            return True
        elif int(s[1] + s[2] + s[0] + s[3]) % 8 == 0:
            return True
        elif int(s[1] + s[2] + s[3] + s[0]) % 8 == 0:
            return True
        elif int(s[1] + s[3] + s[0] + s[2]) % 8 == 0:
            return True
        elif int(s[1] + s[3] + s[2] + s[0]) % 8 == 0:
            return True
        elif int(s[2] + s[0] + s[1] + s[3]) % 8 == 0:
            return True
        elif int(s[2] + s[0] + s[3] + s[1]) % 8 == 0:
            return True
        elif int(s
