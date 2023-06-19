def prime_list(n):
    #n以下の素数のリストを返す
    #エラトステネスの篩
    #素数のリスト
    primes = []
    #0,1は素数ではない
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return primes
