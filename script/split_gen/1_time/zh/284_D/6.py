def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
