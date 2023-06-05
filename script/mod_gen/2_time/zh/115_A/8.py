def get_prime_factor(n):
    prime_factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                prime_factors.append(i)
                n = n // i
                break
    return prime_factors

if __name__ == '__main__':
    get_prime_factor()