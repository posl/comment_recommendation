def getUniqueChar(s):
    if s[0] == s[1]:
        return s[2]
    if s[1] == s[2]:
        return s[0]
    if s[0] == s[2]:
        return s[1]
    return -1

if __name__ == '__main__':
    getUniqueChar()