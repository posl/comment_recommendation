def getStrHash(str):
    hash = 0
    for i in range(len(str)):
        hash += ord(str[i]) * pow(2, i)
    return hash

if __name__ == '__main__':
    getStrHash()