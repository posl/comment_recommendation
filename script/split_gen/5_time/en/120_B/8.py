def get_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors
