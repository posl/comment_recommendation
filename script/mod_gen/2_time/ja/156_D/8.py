def combination(n, r, mod):
    # nCr
    r = min(n - r, r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res

if __name__ == '__main__':
    combination()