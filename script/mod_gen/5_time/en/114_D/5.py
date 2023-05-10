def factorize(n):
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            yield b, e
            b, e = b + 1, 0
    if n > 1:
        yield n, 1

if __name__ == '__main__':
    factorize()