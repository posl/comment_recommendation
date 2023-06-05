def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    isPrime()