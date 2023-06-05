def isHardToRead(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i].islower():
                return False
        else:
            if not s[i].isupper():
                return False
    return True

if __name__ == '__main__':
    isHardToRead()