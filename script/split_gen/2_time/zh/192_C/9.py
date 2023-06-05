def isHardToRead(s):
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i].islower():
                return False
        else:
            if s[i].isupper():
                return False
    return True
