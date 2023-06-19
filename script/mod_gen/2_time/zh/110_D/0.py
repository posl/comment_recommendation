def prime_factorization(n):
    """分解质因数"""
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

if __name__ == '__main__':
    prime_factorization()