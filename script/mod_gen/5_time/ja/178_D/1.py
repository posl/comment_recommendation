def calc_combination_mod(n, r, mod=10**9+7):
    if r > n:
        return 0
    return calc_factorial_mod(n, mod) * pow(calc_factorial_mod(r, mod), mod-2, mod) * pow(calc_factorial_mod(n-r, mod), mod-2, mod) % mod

if __name__ == '__main__':
    calc_combination_mod()