def get_primes(n):
    # n以下の素数を列挙する
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        primes = [2]
        for i in range(3, n+1, 2):
            for p in primes:
                if i%p == 0:
                    break
            else:
                primes.append(i)
        return primes
