def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n%i == 0:
            return

if __name__ == '__main__':
    isprime()