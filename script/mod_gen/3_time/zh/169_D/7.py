def prime_factorization(n):
    if n == 1:
        return [1]
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
n = int(input())
factors = prime_factorization(n)
fact_set = set(factors)
ans = 0
for fact in fact_set:
    tmp = 0
    while n % fact == 0:
        n //= fact
        tmp += 1
    if tmp == 0:
        continue
    i = 1
    while i * i <= tmp:
        if tmp % i == 0:
            if i in fact_set:
                ans += 1
            if tmp // i in fact_set:
                ans += 1
        i += 1
    if tmp * tmp == tmp and tmp in fact_set:
        ans -= 1

if __name__ == '__main__':
    prime_factorization()