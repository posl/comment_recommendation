def get_primes(n):
    primes = []
    for i in range(2, n+1):
        if all([i % p != 0 for p in primes]):
            primes.append(i)
    return primes

if __name__ == '__main__':
    get_primes()