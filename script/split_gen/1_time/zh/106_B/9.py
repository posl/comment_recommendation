def getPrime(n):
    prime = []
    for i in range(2, n+1):
        if isPrime(i):
            prime.append(i)
    return prime
