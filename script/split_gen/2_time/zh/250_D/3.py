def prime_factorization(n):
    result = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            result.append(i)
            n //= i
    if n > 1:
        result.append(n)
    return result
