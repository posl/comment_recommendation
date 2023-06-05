def get_prime_factors(num):
    prime_factors = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            prime_factors.append(i)
            num = num / i
        i = i + 1
    if num > 1:
        prime_factors.append(num)
    return prime_factors
