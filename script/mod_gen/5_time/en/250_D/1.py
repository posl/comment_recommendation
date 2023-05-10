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
N = int(input())
table = prime_factorization(N)
ans = 0
for i in range(len(table)):
    for j in range(i + 1, len(table)):
        if table[i] * table[j] ** 3 <= N:
            ans += 1
print(ans)

if __name__ == '__main__':
    prime_factorization()