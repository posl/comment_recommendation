def prime(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        primes = [2]
        for i in range(3, n + 1, 2):
            for j in range(3, int(i ** 0.5) + 1, 2):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        return primes
