def get_primes(n):
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

if __name__ == '__main__':
    get_primes()