def isWonderfulString(s):
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s[0].islower() and s[1].isupper():
            return True
        else:
            return False
    else:
        if s[0].islower() and s[1].isupper():
            for i in range(2, len(s)):
                if s[i].islower() and s[i-2].islower():
                    return False
                if s[i].isupper() and s[i-2].isupper():
                    return False
            return True
        else:
            return False
s = input()

if __name__ == '__main__':
    isWonderfulString()