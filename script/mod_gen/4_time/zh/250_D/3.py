def get_primes(n):
    primes = []
    is_primes = [True] * (n + 1)
    is_primes[0] = False
    is_primes[1] = False
    for i in range(2, n + 1):
        if is_primes[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_primes[j] = False
    return primes

if __name__ == '__main__':
    get_primes()