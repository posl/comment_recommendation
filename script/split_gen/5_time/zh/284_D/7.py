def getPrimes(n):
    primes = []
    if n < 2:
        return primes
    primes.append(2)
    for i in range(3,n+1):
        flag = True
