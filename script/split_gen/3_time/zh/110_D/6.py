def prime_factorize(n):
    #nの素因数分解を辞書で返す
    if n == 1:
        return {1:1}
    i = 2
    table = {}
    while i * i <= n:
        while n % i == 0:
            n = n // i
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        i += 1
    if n > 1:
        table[n] = 1
    return table
