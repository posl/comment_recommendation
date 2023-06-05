def factorization(n):
    result = []
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            s = 0
            while n % k == 0:
                n //= k
                s += 1
            result.append((k, s))
    if n > 1:
        result.append((n, 1))
    return result

if __name__ == '__main__':
    factorization()