def get_primes(n):
    primes = []
    is_prime = [True] * (n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return primes

if __name__ == '__main__':
    get_primes()