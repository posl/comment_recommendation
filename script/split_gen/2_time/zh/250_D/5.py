def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
N = int(input())
ans = 0
for i in range(1, int(N**0.25)+1):
    if N%i == 0:
        if isPrime(i):
            for j in range(1, int(N**0.25)+1):
                if i**3*j <= N:
                    if isPrime(j):
                        ans += 1
print(ans)
