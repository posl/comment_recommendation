def isPrime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    i = 3
    while i <= num ** 0.5:
        if num %
