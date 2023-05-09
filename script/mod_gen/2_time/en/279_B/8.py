def isSubString(s, t):
    if s == t:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == t[0]:
            return isSubString(s[1:], t[1:])
        elif s[-1] == t[0]:
            return isSubString(s[:-1], t[1:])
        else:
            return False
s = input()
t = input()

if __name__ == '__main__':
    isSubString()