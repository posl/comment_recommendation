def getCharNumber(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if a <= val and val <= z:
        return val - a
    return -1

if __name__ == '__main__':
    getCharNumber()