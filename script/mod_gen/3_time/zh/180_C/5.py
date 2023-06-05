def prime_factorization(n):
    if n <= 1:
        return []
    prime_factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
    return prime_factors
n = int(input())
prime_factors = prime_factorization(n)
ans = set([1])
for prime_factor in prime_factors:
    tmp = set()
    for a in ans:
        tmp.add(a)
        tmp.add(a * prime_factor)
    ans = tmp
ans = list(ans)
ans.sort()
for a in ans:
    print(a)

if __name__ == '__main__':
    prime_factorization()