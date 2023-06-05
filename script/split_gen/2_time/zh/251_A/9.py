def get_prime_number(n):
    prime_number = []
    for i in range(2, n+1):
        for j in prime_number:
            if i % j == 0:
                break
        else:
            prime_number.append(i)
    return prime_number
