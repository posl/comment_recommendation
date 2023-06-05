def get_prime_factor(n):
    factor = []
    if n < 2:
        return factor
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            factor.append(i)
    if n > 1:
        factor.append(n)
    return factor

if __name__ == '__main__':
    get_prime_factor()