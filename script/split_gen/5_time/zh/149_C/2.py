def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i*i <= x:
        if x % i == 0:
            return False
        i += 2
    return True
x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1
