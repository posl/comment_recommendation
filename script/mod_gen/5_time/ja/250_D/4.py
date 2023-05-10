def prime_factorization(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
n = int(input())
table = prime_factorization(n)
count = 0
for i in range(len(table)):
    if table[i] == 2:
        count += 1
print(count)

if __name__ == '__main__':
    prime_factorization()