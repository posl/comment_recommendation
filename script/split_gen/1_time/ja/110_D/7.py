def calc_prime_factorization(n):
    """nの素因数分解を辞書型で返す
    """
    prime_factorization = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factorization[i] = prime_factorization.get(i, 0) + 1
    if n > 1:
        prime_factorization[n] = prime_factorization.get(n, 0) + 1
    return prime_factorization
