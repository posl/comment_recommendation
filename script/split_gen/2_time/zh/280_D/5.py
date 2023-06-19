def get_prime(n):
    prime = []
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, n + 1):
        if is_prime[i] == 1:
            prime.append(i)
            for j in range(i + i, n + 1, i):
                is_prime[j] = 0
    return prime
