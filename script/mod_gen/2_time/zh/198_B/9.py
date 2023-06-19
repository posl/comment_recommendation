def isHuiWen(s):
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if s[0] == s[-1]:
        return isHuiWen(s[1:-1])
    else:
        return False

if __name__ == '__main__':
    isHuiWen()