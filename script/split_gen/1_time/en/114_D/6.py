def prime_factorization(n):
    factorization = []
    for i in range(2, int(n**0.5)+1):
        while n%i == 0:
            n //= i
            factorization.append(i)
    if n != 1:
        factorization.append(n)
    return factorization
n = int(input())
prime = [0]*101
for i in range(2, n+1):
    factorization = prime_factorization(i)
    for j in factorization:
        prime[j] += 1
ans = 0
for i in range(2, 101):
    if prime[i] >= 74:
        ans += 1
    for j in range(2, 101):
        if prime[i] >= 2 and prime[j] >= 24 and i != j:
            ans += 1
        if prime[i] >= 4 and prime[j] >= 14 and i != j:
            ans += 1
        for k in range(2, 101):
            if prime[i] >= 2 and prime[j] >= 4 and prime[k] >= 4 and i != j and i != k and j != k:
                ans += 1
print(ans)
