def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if (n % i) == 0:
            return False
        i += 1
    return True
x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    isPrime()