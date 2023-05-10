def factorize(n):
    # 素因数分解
    # 素因数とその指数をタプルのリストで返す
    # 例：factorize(100) = [(2,2),(5,2)]
    b = 2
    fct = []
    while b*b <= n:
        cnt = 0
        while n%b == 0:
            cnt += 1
            n //= b
        if cnt > 0:
            fct.append((b,cnt))
        b += 1
    if n > 1:
        fct.append((n,1))
    return fct
