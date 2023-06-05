def isPrime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    i = 5
    j = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += j
        j = 6 - j
    return True

if __name__ == '__main__':
    isPrime()