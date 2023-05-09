def calc_exp(exp, a, b):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return calc_exp(exp/2, a, b)**2 % MOD
    else:
        return calc_exp(exp-1, a, b) * a % MOD
