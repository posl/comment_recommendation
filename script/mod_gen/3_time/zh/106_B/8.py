def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True

if __name__ == '__main__':
    isPrime()