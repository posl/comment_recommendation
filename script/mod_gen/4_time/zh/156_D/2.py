def getGCD(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

if __name__ == '__main__':
    getGCD()