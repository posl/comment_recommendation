def isHardToRead(s):
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].isupper() == True:
                return False
        else:
            if s[i].islower() == True:
                return False
    return True

if __name__ == '__main__':
    isHardToRead()