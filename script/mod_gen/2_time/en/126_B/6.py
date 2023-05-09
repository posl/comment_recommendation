def checkYYMM(s):
    if (int(s[2:4]) > 12) or (int(s[2:4]) < 1):
        return False
    return True

if __name__ == '__main__':
    checkYYMM()