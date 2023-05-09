def modpow(a, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return modpow(a * a % mod, n // 2, mod)
    return a * modpow(a, n - 1, mod) % mod

if __name__ == '__main__':
    modpow()