def prime_factorize(n):
    # 素因数分解
    # 戻り値: [[素因数, 指数], ...]
    # 計算量: O(√n)
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            ex = 0
            while n%i==0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n!=1:
        res.append([n, 1])
    return res
n = int(input())
pf = prime_factorize(n)
