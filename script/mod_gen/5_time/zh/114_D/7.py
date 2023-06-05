def factorization(n):
    i = 2
    result = []
    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            result.append([i, ex])
        i += 1
    if n != 1:
        result.append([n, 1])
    return result

if __name__ == '__main__':
    factorization()