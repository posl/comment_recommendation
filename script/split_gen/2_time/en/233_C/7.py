def solve():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, X = map(int, readline().split())
    *A, = map(int, read().split())
    from collections import defaultdict
    from math import gcd
    def prime_factorize(n):
        fct = defaultdict(int)
        for i in range(2, int(n**0.5)+1):
            while n % i == 0:
                n //= i
                fct[i] += 1
        if n > 1:
            fct[n] += 1
        return fct
    fct = prime_factorize(X)
    if not fct:
        print(0)
        return
    # 1つずつの素因数を含む組み合わせの数
    def count(fct, A):
        res = 1
        for p, e in fct.items():
            cnt = 0
            for a in A:
                while a % p == 0:
                    a //= p
                    cnt += 1
            res *= cnt + 1
        return res
    cnt = count(fct, A)
    # 2つ以上の素因数を含む組み合わせの数
    for p, e in fct.items():
        if e == 1:
            continue
        fct2 = fct.copy()
        fct2[p] = 1
        cnt -= count(fct2, A)
    print(cnt)
