def prime_factorization(n):
    # 素因数分解
    # n:整数
    # 戻り値:素因数分解結果
    # 例:prime_factorization(24)
    # 戻り値: [2, 2, 2, 3]
    # 24 = 2^3 * 3^1
    # 例:prime_factorization(25)
    # 戻り値: [5, 5]
    # 25 = 5^2
    # 例:prime_factorization(1)
    # 戻り値: []
    # 1 = 1^0
    # 例:prime_factorization(0)
    # 戻り値: []
    # 0 = 0^0
    # 例:prime_factorization(-1)
    # 戻り値: []
    # -1 = -1^0
    # 例:prime_factorization(-24)
    # 戻り値: []
    # -24 = 2^3 * 3^1
    # 例:prime_factorization(-25)
    # 戻り値: []
    # -25 = 5^2
    if n == 0:
        return []
    elif n < 0:
        return []
    else:
        prime_factorization_list = []
        while n % 2 == 0:
            prime_factorization_list.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                prime_factorization_list.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            prime_factorization_list.append(n)
        return prime_factorization_list
