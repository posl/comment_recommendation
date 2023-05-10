def checkPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5 + 1), 2):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    checkPrime()