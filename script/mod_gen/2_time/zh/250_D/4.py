def prime_factorization(n):
    i = 2
    table = {}
    while i * i <= n:
        while n % i == 0:
            n //= i
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        i += 1
    if n > 1:
        table[n] = 1
    return table

if __name__ == '__main__':
    prime_factorization()