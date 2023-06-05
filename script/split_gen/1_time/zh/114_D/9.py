def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True
