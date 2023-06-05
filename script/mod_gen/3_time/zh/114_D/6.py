def get_primes(n):
    primes = [2]
    for i in range(3, n+1):
        for j in primes:
            if i % j == 0:
                break
            if j > int(i**0.5):
                primes.append(i)
                break
    return primes

if __name__ == '__main__':
    get_primes()