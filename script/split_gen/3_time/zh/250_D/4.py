def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True
N = int(input())
count = 0
for q in range(1, int(N**(1/3))+1):
    if isPrime(q):
        for p in range(1, q):
            if isPrime(p):
                if p*q**3 <= N:
                    count += 1
                else:
                    break
print(count)
