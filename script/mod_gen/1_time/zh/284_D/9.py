def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return

if __name__ == '__main__':
    isPrime()