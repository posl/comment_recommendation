def modpow(a, n, mod): #a^n mod
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modpow(a, n // 2, mod)**2 % mod
    else:
        return a * modpow(a, n - 1, mod) % mod
