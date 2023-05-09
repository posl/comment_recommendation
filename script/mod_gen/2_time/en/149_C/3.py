def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

if __name__ == '__main__':
    isPrime()