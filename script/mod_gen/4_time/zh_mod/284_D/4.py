def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:

if __name__ == '__main__':
    isPrime()