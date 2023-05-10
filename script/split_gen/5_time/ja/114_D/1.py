def prime_factorize(n):
    # 素因数分解
    # 素因数とその個数のタプルのリストを返す
    # 素因数分解した結果を素因数とその個数のタプルのリストで返す
    # 例: 24 → [(2, 3), (3, 1)]
    # 例:  2 → [(2, 1)]
    # 例:  1 → []
    # 例:  0 → []
    if n <= 1:
        return []
    else:
        return [(d, e) for d, e in zip(*factorize(n))]
