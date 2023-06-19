def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True
n = int(input())
ans = 0
for i in range(1, int(n**0.25)+1):
    if isPrime(i):
        for j in range(int(n**(1/3))+1, int(n**0.5)+1):
            if i*j**3 <= n:
                ans += 1
            else:
                break
print(ans)
