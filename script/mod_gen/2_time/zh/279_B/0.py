def isSubString(s,t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    if t in s:
        return True
    else:
        return False

if __name__ == '__main__':
    isSubString()