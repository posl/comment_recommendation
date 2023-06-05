def seven_five(n):
    # 1からnまでの整数の積を求める
    def product(n):
        if n == 1:
            return 1
        else:
            return n * product(n - 1)
    # 素因数分解
    def prime_factorization(n):
        if n == 1:
            return []
        else:
            for i in range(2, n + 1):
                if n % i == 0:
                    return [i] + prime_factorization(n // i)
    # 素因数分解結果を辞書型に変換
    def prime_factorization_dict(n):
        prime_factorization_list = prime_factorization(n)
        prime_factorization_dict = {}
        for i in prime_factorization_list:
            prime_factorization_dict[i] = prime_factorization_dict.get(i, 0) + 1
        return prime_factorization_dict
    # 素因数分解結果の約数の個数を求める
    def divisor_count(n):
        prime_factorization_dict_n = prime_factorization_dict(n)
        divisor_count = 1
        for i in prime_factorization_dict_n.values():
            divisor_count *= i + 1
        return divisor_count
    # 75の約数の個数を求める
    def seven_five_count(n):
        prime_factorization_dict_n = prime_factorization_dict(n)
        prime_factorization_dict_n_values = prime_factorization_dict_n.values()
        seven_five_count = 0
        for i in prime_factorization_dict_n_values:
            if i >= 74:
                seven_five_count += 1
            for j in prime_factorization_dict_n_values:
                if i != j and i >= 24 and j >= 2:
                    seven_five_count += 1
                for k in prime_factorization_dict_n_values:
                    if i != j != k and i >= 14 and j >= 4 and k >= 4:
                        seven_five_count += 1
        return seven_five_count
    # 1からnまでの整数の積を求める
    product_n = product(n)
    # print(product_n)
    # 75の約数の個数を求める
