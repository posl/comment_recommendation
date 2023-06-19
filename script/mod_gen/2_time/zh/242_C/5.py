def getNumber(n):
    if n < 2:
        return 0
    elif n == 2:
        return 25
    else:
        return (25 * pow(26, n-2, 998244353)) % 998244353

if __name__ == '__main__':
    getNumber()