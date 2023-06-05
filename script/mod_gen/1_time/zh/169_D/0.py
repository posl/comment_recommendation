def prime_factorization(N):
    prime_factor = []
    i = 2
    while i * i <= N:
        while N % i == 0:
            prime_factor.append(i)
            N //= i
        i += 1
    if N > 1:
        prime_factor.append(N)
    return prime_factor

if __name__ == '__main__':
    prime_factorization()