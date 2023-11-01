def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

if __name__ == '__main__':
    isPrime()