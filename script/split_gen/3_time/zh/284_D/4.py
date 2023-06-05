def isPrime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
