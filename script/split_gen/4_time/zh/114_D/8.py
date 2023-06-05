def factorization(n):
    if n == 1:
        return {}
    i = 2
    table = {}
    while i * i <= n:
        while n % i == 0:
            n //= i
            if i not in table:
                table[i] = 0
            table[i] += 1
        i += 1
    if n > 1:
        table[n] = 1
    return table
