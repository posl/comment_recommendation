def prime_factorization(n):
    """素因数分解する関数
    引数
    n:整数
    返り値
    list:素因数分解の結果
    """
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