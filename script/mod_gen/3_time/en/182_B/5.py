def getGCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return getGCD(b, a % b)

if __name__ == '__main__':
    getGCD()