def modpow(x, n, mod):
    """x^nをmodで割った余りを求める"""
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

if __name__ == '__main__':
    modpow()