def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True
x = int(input())
while not isPrime(x):
    x += 1
print(x)
