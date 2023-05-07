def get_prime_factorization(n):
    prime_factorization = []
    for i in range(2, int(n**0.5)+1):
        if n == 1:
            break
        while n%i == 0:
            prime_factorization.append(i)
            n //= i
    if n != 1:
        prime_factorization.append(n)
    return prime_factorization
