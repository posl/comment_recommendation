def check_split(s):
    if s[0] == '0' and s[1] == '1':
        if s[2] == '0' and s[3] == '1':
            return True
        elif s[3] == '0' and s[4] == '1':
            return True
        elif s[4] == '0' and s[5] == '1':
            return True
        elif s[5] == '0' and s[6] == '1':
            return True
        elif s[6] == '0' and s[7] == '1':
            return True
        elif s[7] == '0' and s[8] == '1':
            return True
        elif s[8] == '0' and s[9] == '1':
            return True
        else:
            return False
    else:
        return False
