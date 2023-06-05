def getN(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 6:
        return 1
    if n == 9:
        return 1
    if n < 6:
        return 1 + getN(n-1)
    if n < 9:
        return 1 + getN(n-6)
    if n < 36:
        return min(1 + getN(n-6), 1 + getN(n-9), 1 + getN(n-1))
    if n < 81:
        return min(1 + getN(n-9), 1 + getN(n-1))
    if n < 216:
        return 1 + getN(n-6)
    if n < 729:
        return 1 + getN(n-9)
    if n < 1296:
        return min(1 + getN(n-9), 1 + getN(n-1))
    if n < 7776:
        return 1 + getN(n-6)
    if n < 6561:
        return 1 + getN(n-9)
    if n < 46656:
        return min(1 + getN(n-9), 1 + getN(n-1))
    if n < 59049:
        return 1 + getN(n-6)
    if n < 279936:
        return 1 + getN(n-9)
    if n < 531441:
        return min(1 + getN(n-9), 1 + getN(n-1))
    if n < 1679616:
        return 1 + getN(n-6)
    if n < 4782969:
        return 1 + getN(n-9)
    if n < 100000:
        return min(1 + getN(n-9), 1 + getN(n-1))
    return 0

if __name__ == '__main__':
    getN()