def get_prime_factors(num):
    prime_factors = []
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.append(i)
                num = num // i
                break
    return prime_factors
