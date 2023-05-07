def isHardToRead(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower():
                pass
            else:
                return False
        else:
            if s[i].isupper():
                pass
            else:
                return False
    return True

if __name__ == '__main__':
    isHardToRead()