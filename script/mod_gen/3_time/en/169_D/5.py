def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
n = int(input())
factors = get_prime_factors(n)
factor_count = {}
for i in factors:
    if i not in factor_count:
        factor_count[i] = 0
    factor_count[i] += 1
max_count = 0
for i in factor_count:
    count = 0
    while factor_count[i] > 0:
        factor_count[i] -= i
        count += 1
    if count > max_count:
        max_count = count
print(max_count)

if __name__ == '__main__':
    get_prime_factors()