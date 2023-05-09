def modpow(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        return modpow(a * a % mod, b // 2, mod)
    return a * modpow(a, b - 1, mod) % mod
