def get_permutation(n, r, mod):
    if r > n:
        return 0
    return (fact[n] * fact_inv[n-r]) % mod

if __name__ == '__main__':
    get_permutation()