def eratosthenes(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        primes = [2]
        candidates = list(range(3, n + 1, 2))
        while candidates[0] ** 2 <= n:
            p = candidates[0]
            primes.append(p)
            candidates = [c for c in candidates if c % p != 0]
        primes.extend(candidates)
        return primes

if __name__ == '__main__':
    eratosthenes()