def isPrime(n):
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    isPrime()