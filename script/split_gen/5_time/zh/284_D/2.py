def get_prime_list(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list
