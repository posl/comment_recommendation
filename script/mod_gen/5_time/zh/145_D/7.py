def modpow(x, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return modpow(x * x % mod, n // 2, mod)
    else:
        return x * modpow(x, n - 1, mod) % mod

if __name__ == '__main__':
    modpow()