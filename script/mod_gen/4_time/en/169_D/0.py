def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N = int(input())
factors = prime_factorize(N)
ans = 0
for i in range(len(factors)):
    if i == 0:
        ans += factors[i] - 1
    else:
        ans += factors[i]
print(ans)
import math
N = int(input())
ans = 0
for i in range(2, int(math.sqrt(N)) + 1):
    while N % i == 0:
        N = N // i
        ans += 1

if __name__ == '__main__':
    prime_factorize()