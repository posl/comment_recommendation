def isPrime(x):
    if x == 2:
        return True
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    isPrime()