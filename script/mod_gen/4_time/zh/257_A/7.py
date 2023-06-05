def getStr(n):
    s = ''
    for i in range(n):
        s += chr(65+i)*n
    return s

if __name__ == '__main__':
    getStr()