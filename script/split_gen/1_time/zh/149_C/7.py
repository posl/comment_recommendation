def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
x = int(input())
while not isPrime(x):
    x += 1
print(x)
