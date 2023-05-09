def get_permutation(n, r, mod):
    if r > n:
        return 0
    return (fact[n] * fact_inv[n-r]) % mod
