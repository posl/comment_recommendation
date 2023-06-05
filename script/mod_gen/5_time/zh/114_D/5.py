def prime_factorization(n):
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n //= 2
    f = 3
    while f ** 2 <= n:
        if n % f == 0:
            prime_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_list.append(n)
    return prime_list

if __name__ == '__main__':
    prime_factorization()