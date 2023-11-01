def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    else:
        for i in range(3, i
