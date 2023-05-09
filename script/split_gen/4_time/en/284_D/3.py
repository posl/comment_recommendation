def prime_factorization(n):
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
T = int(input())
for _ in range(T):
    N = int(input())
    table = prime_factorization(N)
    p = table[0]
    q = table[1]
    print(p, q)
