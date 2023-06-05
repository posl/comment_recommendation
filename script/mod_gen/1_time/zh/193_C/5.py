def prime_factorization(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return [i] + prime_factorization(n // i)
        return [n]

if __name__ == '__main__':
    prime_factorization()