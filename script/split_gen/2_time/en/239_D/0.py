def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
takahashi = B - A + 1
aoki = D - C + 1
takahashi_primes = 0
aoki_primes = 0
for i in range(A, B + 1):
    if is_prime(i):
        takahashi_primes += 1
for i in range(C, D + 1):
    if is_prime(i):
        aoki_primes += 1
