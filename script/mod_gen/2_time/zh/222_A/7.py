def addZero(n):
    n = str(n)
    while len(n) < 4:
        n = '0' + n
    return n

if __name__ == '__main__':
    addZero()