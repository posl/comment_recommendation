def prime_factorization(n):
    a = 2
    b = 0
    while a * a <= n:
        while n % a == 0:
            b += 1
            n //= a
        a += 1
    if n > 1:
        b += 1
    return b
n = int(input())
ans = 0
for i in range(1, n + 1):
    if prime_factorization(i) >= 4 and prime_factorization(i) <= 14:
        ans += 1
print(ans)
